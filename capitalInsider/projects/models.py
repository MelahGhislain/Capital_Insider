from django.db import models

# Create your models here.
class Projects(models.Model):
    client = models.CharField(max_length=50, blank=False,null=False)
    year_completed = models.DateTimeField(blank=True,null=True)
    value = models.FloatField(blank=True,null=True)
    adviser = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(null=False,blank=False)
    main_image = models.ImageField(blank=False, null=False)
    image1 = models.ImageField(blank=True, null=True)
    image2 = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title