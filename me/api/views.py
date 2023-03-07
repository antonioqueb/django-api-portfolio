from me.models import Me
from rest_framework.viewsets import ModelViewSet
from me.api.serializers import MeSerializer

class MeList(ModelViewSet):
    queryset = Me.objects.all()
    serializer_class = MeSerializer


class MeDetail(ModelViewSet):
    queryset = Me.objects.all()
MeSerializer  