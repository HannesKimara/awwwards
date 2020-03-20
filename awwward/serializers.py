from rest_framework import serializers

from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    backdrop_image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Project
        fields = (
            'title',
            'description',
            'backdrop_image_url',
            'website_url',
            'posted_at',
            'total_design',
            'total_content',
            'total_content',
            'total_score'
        )

    def get_image_url(self, obj):
        return obj.backdrop_image.url