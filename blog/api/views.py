from rest_framework.viewsets import ModelViewSet
from blog.api.serializers import BlogSerializer
from blog.models import Blog


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer