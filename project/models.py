from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    demo_url = models.CharField(max_length=255)
    github_url = models.CharField(max_length=255)
    details = models.TextField()
    technologies = models.JSONField()
    languages = models.JSONField()
    image_url = models.ImageField( blank='', default="" , upload_to='project')
 
    def __str__(self):
            return self.title