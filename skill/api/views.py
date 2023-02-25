from rest_framework.viewsets import ModelViewSet
from skill.api.serializers import SkillSerializer
from skill.models import Skill


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer