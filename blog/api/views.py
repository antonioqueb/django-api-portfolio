from rest_framework import viewsets
from blog.models import Comment, BlogPost, BlogImage
from blog.api.serializers import CommentSerializer, BlogPostSerializer, BlogImageSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogImageViewSet(viewsets.ModelViewSet):
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer
