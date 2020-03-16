from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index(request):
    return render(request, 'index.html', {'sites': [1, 2, 3, 4, 5, 6, 7, 7, 8, 9,10, 11]})


def profile(request, username):
    return render(request, 'profile.html')


@login_required(login_url='/accounts/login/')
def account(request):
    return render(request, 'account.html')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('index')