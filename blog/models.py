from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from PIL import Image
import random
import io

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Comment(MPTTModel):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    image = models.ImageField(upload_to='blog', null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def save(self, *args, **kwargs):
        if not self.image:
            # Generar una imagen de gradiente de colores aleatorios
            width, height = 30, 30
            img = Image.new('RGB', (width, height))
            pixels = img.load()
            color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for i in range(width):
                for j in range(height):
                    pixels[i, j] = (int(color1[0] * (width - i) / width + color2[0] * i / width),
                                    int(color1[1] * (width - i) / width + color2[1] * i / width),
                                    int(color1[2] * (width - i) / width + color2[2] * i / width))

            # Guardar la imagen generada en el campo de imagen del comentario
            image_file = io.BytesIO()
            img.save(image_file, format='JPEG')
            self.image.save(f'{self.id}.jpg', image_file)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    hashtags = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    image_url = models.ImageField(blank='', default="", upload_to='blog')
    comments = models.ManyToManyField('blog.Comment', related_name='blogpost_comments')
    categories = models.ManyToManyField('blog.Category', related_name='blogpost_categories')

    def __str__(self):
        return self.title

class BlogImage(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    image = models.ImageField(blank='', default="", upload_to='blog')

    def __str__(self):
        return self.image.name
