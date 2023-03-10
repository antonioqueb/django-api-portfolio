from django.db import models

class ContactMe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email + ' - ' + self.name + ' - ' + self.message
