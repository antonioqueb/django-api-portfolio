from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, CommentViewSet, BlogPostViewSet, BlogImageViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'comments', CommentViewSet)
router.register(r'blogposts', BlogPostViewSet)
router.register(r'blogimages', BlogImageViewSet)
