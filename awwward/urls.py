from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('account', views.account, name='account'),
    path('accounts/logout', views.logout_user, name="logout"),
]