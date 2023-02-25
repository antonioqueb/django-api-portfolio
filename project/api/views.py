from rest_framework.viewsets import ModelViewSet
from project.api.serializers import ProjectSerializer
from project.models import Project


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer