from django.db import models

# Create your models here.
class AboutUs(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)


class  Expert(models.Model):
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    position = models.CharField(max_length=100, null=False, blank=False)
