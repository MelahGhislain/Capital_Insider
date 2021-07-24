from django.contrib import admin

from .models import SocialNetwork, ContactInfo, FinancialAdvisor

# Register your models here.
admin.site.register(SocialNetwork)
admin.site.register(ContactInfo)
admin.site.register(FinancialAdvisor)
