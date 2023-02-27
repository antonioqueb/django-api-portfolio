from rest_framework.routers import DefaultRouter
from contact.api.views import ContactViewSet

router = DefaultRouter()
router.register(r'contact', ContactViewSet, basename='contact')