from rest_framework.viewsets import ModelViewSet
from education.api.serializers import EducationSerializer
from education.models import Education


class EducationViewSet(ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer