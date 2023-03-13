from django.db import models

class Me(models.Model):
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    profile = models.ImageField(blank=True, default='', upload_to='me')
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    galery = models.ImageField(blank=True, default='', upload_to='me')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
