from rest_framework.routers import DefaultRouter
from blog.api.views import CommentViewSet, BlogPostViewSet, BlogImageViewSet

router = DefaultRouter()
router.register(r'comments', CommentViewSet)
router.register(r'post', BlogPostViewSet)
router.register(r'images', BlogImageViewSet)

