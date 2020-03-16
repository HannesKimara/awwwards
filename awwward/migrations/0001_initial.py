# Generated by Django 3.0.4 on 2020-03-16 09:54

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('backdrop_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='backdrop_image')),
                ('website_url', models.URLField(max_length=32)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_score', models.FloatField()),
                ('usability_score', models.FloatField()),
                ('content_score', models.FloatField()),
                ('user_total_score', models.FloatField()),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awwward.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', cloudinary.models.CloudinaryField(default='image/upload/v1583754861/person_placeholder_l8auvx.jpg', max_length=255, verbose_name='profile_photo')),
                ('bio', models.TextField(default='')),
                ('country', models.CharField(max_length=64)),
                ('website_url', models.URLField(blank=True, max_length=32)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='screenshots')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awwward.Project')),
            ],
        ),
    ]