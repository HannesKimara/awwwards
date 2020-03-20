from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    backdrop_image_url = serializers.SerializerMethodField('get_image_url')
    project_id = serializers.SerializerMethodField('get_id')

    class Meta:
        model = Project
        fields = (
            'project_id',
            'title',
            'description',
            'backdrop_image_url',
            'website_url',
            'total_design',
            'total_usability',
            'total_content',
            'posted_at',
            'total_design',
            'total_content',
            'total_content',
            'total_score'
        )

    def get_image_url(self, obj):
        return obj.backdrop_image.url

    def get_id(self, obj):
        return obj.id