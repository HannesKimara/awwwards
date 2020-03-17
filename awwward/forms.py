from django import forms

from .models import Profile, Project


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['country', 'user']
        fields = ['photo', 'bio', 'website_url']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'backdrop_image', 'website_url']