from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import Http404
from datetime import date
from statistics import mean

from ..models import Profile, Project, User, Rating
from ..forms import ProfileForm, ProjectForm, RatingForm


def index(request):
    projects = Project.objects.all()
    top_site = Project.objects.filter(
        posted_at__date=date.today()
    ).order_by('-total_score').first()
    if top_site is None:
        top_site = Project.objects.order_by('-total_score').first()
    return render(request, 'index.html', {
        'projects': projects,
        'top_site': top_site,
        'today_date': date.today().strftime('%m %d %Y')
        })


def profile(request, username):
    search_user = User.objects.filter(username=username).first()
    projects = Project.objects.filter(user=search_user)
    if search_user is None:
        raise Http404()

    return render(request, 'profile.html', {
        'user': search_user,
        'projects': projects
        })


@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    user_profile = Profile.objects.filter(user=current_user).first()

    if user_profile is None:
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            print("I got the form")
            if form.is_valid():
                print("Form was valid")
                u_profile = form.save(commit=False)
                u_profile.user = current_user
                u_profile.save()

                return redirect("account")

        form = ProfileForm()
        return render(request, 'create_profile.html', {'form': form})
    else:
        return redirect('account')


@login_required(login_url='/accounts/login/')
def account(request):
    current_user = request.user
    user_profile = Profile.objects.filter(user=current_user).first()

    if user_profile is None:
        print("No profile found for user")
        return redirect('create_profile')
    else:
        user_projects = current_user.project_set.all()
        return render(request, 'account.html', {
            'user': current_user,
            'projects': user_projects
            })


@login_required(login_url='/accounts/login/')
def new_site(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            print("That's a valid form you got there")
            u_project = form.save(commit=False)
            u_project.user = current_user
            u_project.save()

            return redirect("account")
    else:
        form = ProjectForm()
        return render(request, 'new_site.html', {'form': form})


def view_site(request, site_id):
    search_site = Project.objects.filter(pk=site_id).first()
    if search_site is None:
        raise Http404()

    return render(request, 'view_site.html', {'site': search_site})


@login_required(login_url='/accounts/login/')
def rate_site(request, project_id):
    current_user = request.user
    curr_project = Project.objects.filter(pk=project_id).first()

    if curr_project is None:
        raise Http404()

    user_site_rating = Rating.objects.filter(
        project = curr_project,
        user = current_user
        ).first()

    if request.method == "POST":
        if user_site_rating is not None:
            form = RatingForm(request.POST, instance = user_site_rating)
            form.save(commit = False)
            all_ratings = (user_site_rating.design_score, user_site_rating.usability_score, user_site_rating.content_score)
            user_site_rating.user_total_score = mean(list(all_ratings))
            user_site_rating.save()

            curr_project.total_design = mean([rating.design_score for rating in Rating.objects.all()])
            curr_project.total_usability = mean([rating.usability_score for rating in Rating.objects.all()])
            curr_project.total_content = mean([rating.content_score for rating in Rating.objects.all()])
            curr_project.total_score = mean((curr_project.total_design, curr_project.total_usability, curr_project.total_content))
            curr_project.save()
            
        else:
            form = RatingForm(request.POST)
            u_rating = form.save(commit=False)
            u_rating.user = current_user
            u_rating.project = curr_project
            u_rating.user_total_score = mean(list((
                u_rating.design_score,
                u_rating.usability_score,
                u_rating.content_score
            )))
            u_rating.save()
            curr_project.total_design = mean([rating.design_score for rating in Rating.objects.all()])
            curr_project.total_usability = mean([rating.usability_score for rating in Rating.objects.all()])
            curr_project.total_content = mean([rating.content_score for rating in Rating.objects.all()])
            curr_project.total_score = mean((curr_project.total_design, curr_project.total_usability, curr_project.total_content))
            curr_project.save()

    return redirect('view_site', curr_project.id)

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('index')