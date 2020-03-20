from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('account', views.account, name='account'),
    path('account/create', views.create_profile, name="create_profile"),
    path('accounts/logout', views.logout_user, name="logout"),
    path('site/new', views.new_site, name="new_site"),
    path('site/<str:site_id>', views.view_site, name="view_site"),
    path('site/vote/<int:project_id>', views.rate_site, name="rate_site"),
    path('api/projects', views.ProjectView.as_view(), name="api_projects"),
    path('api/projects/<int:project_id>', views.ProjectSingle.as_view(), name="single_project"),
]