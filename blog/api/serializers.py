from rest_framework import serializers
from blog.models import Category, Comment, BlogPost, BlogImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'blogposts']
        # incluye los BlogPost relacionados en la respuesta
        depth = 1

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'blogpost']
        # incluye el BlogPost relacionado en la respuesta
        depth = 1

class BlogPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'pub_date', 'category', 'comments']

class BlogImageSerializer(serializers.ModelSerializer):
    blogpost = BlogPostSerializer(read_only=True)

    class Meta:
        model = BlogImage
        fields = ['id', 'image', 'description', 'blogpost']
