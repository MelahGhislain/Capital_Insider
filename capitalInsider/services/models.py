from django.db import models

# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    description = models.TextField(null=False)
    cash_flow_statement = models.TextField()
    balance_sheet_statement = models.TextField()
    income_statement = models.TextField()
    brainstorming = models.TextField()
    plannification = models.TextField()
    hard_work = models.TextField()
    success = models.TextField()

class Brochures(models.Model):
    PDFfile = models.FileField()
    DOCfile = models.FileField()
