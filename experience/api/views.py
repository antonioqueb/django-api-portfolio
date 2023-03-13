from rest_framework.viewsets import ModelViewSet
from experience.api.serializers import ExperienceSerializer
from experience.models import Experience

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import BasicAuthentication


class ExperienceViewSet(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer