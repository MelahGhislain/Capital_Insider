from django.shortcuts import render
from .models import FinancialAdvisor, ContactInfo, SocialNetwork
from .forms import ContactForm
from django.views import View
from django.http import  HttpResponseRedirect
from django.core.mail import  send_mail
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ContactView(LoginRequiredMixin, View):
    login_url = 'login'
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
            number = form.cleaned_data['phone_num']
            message = form.cleaned_data['message']
            name_phone = username + " " + number
            try:
                send_mail(
                    name_phone, # subject
                    message, # message
                    email, # from email
                    ["melahghislain17@gmail.com"], # to email : can take more than one email
                )
            except Exception as e:
                print(f'============>>>>>>>>> {e}')
            
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

