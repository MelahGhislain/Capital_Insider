from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)
    message = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name



class News(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    news_detail = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=False, null=False)
    # comments = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

