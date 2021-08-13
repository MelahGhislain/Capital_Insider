from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    news_detail = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=False, null=False)
