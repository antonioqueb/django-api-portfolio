from rest_framework.routers import DefaultRouter
from me.api.views import MeList, MeDetail
router = DefaultRouter()

router.register(r'me', MeList, basename='me')
