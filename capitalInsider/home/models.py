from django.db import models

# Create your models here.
class Partner(models.Model):
    logo = models.ImageField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.logo.name

