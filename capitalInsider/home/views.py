from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import  send_mail
from about.models import AboutUs, Expert
from services.models import Services
from projects.models import Projects
from .models import Partner
from news.models import News
from .forms import GetCallForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def homePage(request):
    services = Services.objects.all()
    projects = Projects.objects.all()
    experts = Expert.objects.all()
    partners = Partner.objects.all()
    news = News.objects.all().order_by('-date')
    form = GetCallForm()
    if request.method == "POST":
        form = GetCallForm(request.POST)
        if form.is_valid():
            select = form.cleaned_data['select']
            phone = form.cleaned_data['phone']
            name = form.cleaned_data['name']
            # send an email
            ####################################
            # send_mail(
            #     username, # subject
            #     message, # message
            #     email, # from email
            #     ["melahghislain17@gmail.com"], # to email
            # )

            return HttpResponseRedirect("/")
    context = {
        "services": services,
        "projects": projects,
        "experts": experts,
        "partners": partners,
        'news': news,
        'form': form,
    }
    return render(request, "home/index.html", context)