from rest_framework.viewsets import ModelViewSet
from education.api.serializers import EducationSerializer
from education.models import Education

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import BasicAuthentication


class EducationViewSet(ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer