from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import ProjectSerializer
from ..models import Project


class ProjectView(APIView):
    def get(self, request):
        all_proj = Project.objects.all()
        serializer = ProjectSerializer(all_proj, many=True)
        return Response(serializer.data)


class ProjectSingle(APIView):
    def get(self, request, project_id):
        search_project = Project.objects.filter(pk = project_id).first()
        serializer = ProjectSerializer(search_project)
        return Response(serializer.data)