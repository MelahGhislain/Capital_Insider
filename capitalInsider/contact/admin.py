from django.contrib import admin

from .models import SocialNetwork, ContactInfo, FinancialAdvisor, Map

# Register your models here.
admin.site.register(SocialNetwork)
admin.site.register(ContactInfo)
admin.site.register(FinancialAdvisor)
admin.site.register(Map)
