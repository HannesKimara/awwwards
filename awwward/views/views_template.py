from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import Http404
from datetime import date

from ..models import Profile, Project, User
from ..forms import ProfileForm, ProjectForm


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


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('index')