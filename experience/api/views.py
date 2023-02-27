from rest_framework.viewsets import ModelViewSet
from experience.api.serializers import ExperienceSerializer
from experience.models import Experience


class ExperienceViewSet(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer