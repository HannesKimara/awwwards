from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import ProjectSerializer
from ..models import Project


class ProjectView(APIView):
    def get(self, request):
        all_proj = Project.objects.all()
        serializer = ProjectSerializer(all_proj, many=True)
        return Response(serializer.data)