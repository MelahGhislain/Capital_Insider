from django.db import models

# Create your models here.
class SocialNetwork(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class ContactInfo(models.Model):
    location = models.CharField(max_length=150)
    administration_phone_num = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.location

class FinancialAdvisor(models.Model):
    position = models.CharField(max_length=50)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.position

class MailUs(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_num = models.CharField(max_length=50)
    message = models.TextField(max_length=250)
