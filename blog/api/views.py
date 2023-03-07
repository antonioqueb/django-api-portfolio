from rest_framework.viewsets import ModelViewSet
from blog.models import Category, Comment, BlogPost, BlogImage
from .serializers import CategorySerializer, CommentSerializer, BlogPostSerializer, BlogImageSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogPostViewSet(ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogImageViewSet(ModelViewSet):
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer
