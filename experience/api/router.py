from rest_framework.routers import DefaultRouter
from experience.api.views import ExperienceViewSet

router = DefaultRouter()
router.register(r'experience', ExperienceViewSet, basename='experience')