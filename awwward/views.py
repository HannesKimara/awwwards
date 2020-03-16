from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Profile
from .forms import ProfileForm


def index(request):
    return render(request, 'index.html', {'sites': [1, 2, 3, 4, 5, 6, 7, 7, 8, 9,10, 11]})


def profile(request, username):
    return render(request, 'profile.html')


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
        print("profile found for user")
        return render(request, 'account.html', {'user':current_user})


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('index')