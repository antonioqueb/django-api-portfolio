from rest_framework import serializers
from blog.models import Comment, BlogPost, BlogImage

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImage
        fields = '__all__'
