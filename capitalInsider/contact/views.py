from django.shortcuts import render
from .models import FinancialAdvisor, ContactInfo, SocialNetwork
# Create your views here.
def contactPage(request):
    advisors = FinancialAdvisor.objects.all()
    contact = ContactInfo.objects.last()
    social_networks = SocialNetwork.objects.all()
    return render(request, "contact/index.html", {
        "advisors": advisors,
        "contact": contact,
        "socials": social_networks,
    })