from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """
    Profiles within the database are represented by this model
    """
    photo = CloudinaryField(
        'profile_photo',
        default="image/upload/v1583754861/person_placeholder_l8auvx.jpg")
    bio = models.TextField(default='')
    country = models.CharField(max_length=64)
    website_url = models.URLField(max_length=32, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Project(models.Model):
    """
    Projects within the database are represented by this model
    """
    title = models.CharField(max_length=64)
    description = models.TextField()
    backdrop_image = CloudinaryField('backdrop_image')
    website_url = models.URLField(max_length=32)
    posted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.FloatField(default=0)

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()


class Image(models.Model):
    """
    Image within the database are represented by this model

    Args: 
        image : Image from ImageField
        project (Project:models.Model): Relational object Project

    Methods:
        save_image : Save object to Database. Refer to help(save_image)
        delete_image : Delete object from Database. Refer to help(delete_image)
    """
    image = CloudinaryField('screenshots')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


class Rating(models.Model):
    """
    Project ratings within the database are represented by this model
    
    Args:
        design_score (float) : Design rating in inclusive range 0.0-10.0
        usability_score (float) : Usability rating in inclusive range 0.0-10.0
        content_score (float) : Content rating in inclusive range 0.0 - 10.0
        user_total_score (float) : Mean of design_score,
                        usability_score, content_score
        project (Project:models.Model): Relational object Project
        user (User:models.Model) : Relational object User

    Methods:
        save_rating : Save object to Database. 
                        Refer to help(save_rating)
        delete_rating : Delete object from Database. 
                        Refer to help(delete_rating)
    """
    design_score = models.FloatField()
    usability_score = models.FloatField()
    content_score = models.FloatField()
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_total_score = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_rating(self):
        self.save()

    def delete_rating(self):
        self.delete()