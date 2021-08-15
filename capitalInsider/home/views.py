from django.shortcuts import render
from about.models import AboutUs, Expert
from services.models import Services
from projects.models import Projects
from .models import Partner
from news.models import News

# Create your views here.

def homePage(request):
    services = Services.objects.all()
    projects = Projects.objects.all()
    experts = Expert.objects.all()
    partners = Partner.objects.all()
    news = News.objects.all().order_by('-date')
    context = {
        "services": services,
        "projects": projects,
        "experts": experts,
        "partners": partners,
        'news': news,
    }
    return render(request, "home/index.html", context)