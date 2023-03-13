from django.db import models

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    logo_url = models.ImageField(blank=True , upload_to='education')
    website_url = models.CharField(max_length=200)

    def __str__(self):
        return self.degree + " at " + self.institution
