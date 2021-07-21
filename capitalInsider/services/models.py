from django.db import models

# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=50)
    service_image = models.ImageField(null=False, blank=False)
    image = models.ImageField(blank=True)
    description = models.TextField(null=False)
    cash_flow_statement = models.TextField(null=True, blank=True)
    balance_sheet_statement = models.TextField(null=True, blank=True)
    income_statement = models.TextField(null=True, blank=True)
    brainstorming = models.TextField(null=True, blank=True)
    plannification = models.TextField(null=True, blank=True)
    hard_work = models.TextField(null=True, blank=True)
    success = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Brochures(models.Model):
    PDFfile = models.FileField(blank=False, null=False)
    DOCfile = models.FileField(blank=False, null=False)
