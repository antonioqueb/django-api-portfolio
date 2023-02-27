from rest_framework.routers import DefaultRouter
from .views import EducationViewSet

router = DefaultRouter()
router.register(r'experience', EducationViewSet, basename='experience')