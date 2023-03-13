from rest_framework.viewsets import ModelViewSet
from skill.api.serializers import SkillSerializer
from skill.models import Skill

from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import BasicAuthentication


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer