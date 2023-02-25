from django.db import models
from django.urls import reverse

class Contact(models.Model):
    email = models.EmailField()
    phone_number = models.IntegerField()
    linkedin_url = models.CharField(max_length=50)
    github_url = models.CharField(max_length=50)

    def __str__(self):
        return self.email
