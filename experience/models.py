from django.db import models

class Experience(models.Model):
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=80)
    startDate = models.DateField()
    endDate = models.DateField()
    logoUrl = models.ImageField( blank='', default="" , upload_to='experience')

    def __str__(self):
        return self.company

    class Meta:
        verbose_name_plural = 'Experiences'
