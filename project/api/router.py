from rest_framework.routers import DefaultRouter
from project.api.views import ProjectViewSet



router = DefaultRouter()

router.register(r'project', ProjectViewSet, basename='project')
