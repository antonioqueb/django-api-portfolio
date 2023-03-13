from rest_framework.viewsets import ModelViewSet
from project.api.serializers import ProjectSerializer
from project.models import Project

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import BasicAuthentication


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    