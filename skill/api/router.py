from rest_framework.routers import DefaultRouter
from skill.api.views import SkillViewSet

router = DefaultRouter()
router.register(r'skill', SkillViewSet, basename='skill'),
