from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    logo_url = models.ImageField( blank='', default="" , upload_to='skill')
    experience = models.CharField(max_length=200)

    
    def __str__(self):
        return self.name
