from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    hashtags = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    image_url = models.ImageField(upload_to='static/logos/')
    comments = models.ManyToManyField('blog.Comment', related_name='blogpost_comments')

    def __str__(self):
        return self.title

class BlogImage(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/blog_images/')

    def __str__(self):
        return self.image.name
