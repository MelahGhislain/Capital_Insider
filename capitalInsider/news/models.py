from django.db import models

# Create your models here.

# if category will be needed

# class Category(models.Model):
#     category = models.CharField(max_length=150)

class News(models.Model):
    title = models.CharField(max_length=200)
    # category = models.ForeignKey(Category, on_delete=models.SET_NUL)
    date = models.DateField(auto_now_add=True)
    news_detail = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=False, null=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)
    message = models.TextField(blank=False, null=False)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

