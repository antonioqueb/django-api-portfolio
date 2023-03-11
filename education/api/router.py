from rest_framework.routers import DefaultRouter
from education.api.views import EducationViewSet

router = DefaultRouter()
router.register(r'experience', EducationViewSet, basename='experience')