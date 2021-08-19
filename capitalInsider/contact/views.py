from django.shortcuts import render
from .models import FinancialAdvisor, ContactInfo, SocialNetwork
from .forms import ContactForm
from django.views import View
from django.http import  HttpResponseRedirect
from django.core.mail import  send_mail

# Create your views here.
class ContactView(View):
    def get(self, request):
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

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            # number = form.cleaned_data['phone_num']
            message = form.cleaned_data['message']
            send_mail(
                username, # subject
                message, # message
                email, # from email
                ["melahghislain17@gmail.com"], # to email
            )
            
            return HttpResponseRedirect("/contact")

        advisors = FinancialAdvisor.objects.all()
        contact = ContactInfo.objects.last()
        social_networks = SocialNetwork.objects.all()

        return render(request, "contact/index.html", {
            "advisors": advisors,
            "contact": contact,
            "socials": social_networks,
            "form": form,
        })

