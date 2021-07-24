from django.shortcuts import render
from .models import FinancialAdvisor, ContactInfo, SocialNetwork
from .forms import ContactForm


# Create your views here.
def contactPage(request):
    advisors = FinancialAdvisor.objects.all()
    contact = ContactInfo.objects.last()
    social_networks = SocialNetwork.objects.all()

    form = ContactForm()

    return render(request, "contact/index.html", {
        "advisors": advisors,
        "contact": contact,
        "socials": social_networks,
        "form": form,
    })