from django.shortcuts import render
from about.models import AboutUs, Expert
from services.models import Services
from projects.models import Projects
from .models import Partner
from news.models import News
from .forms import GetCallForm

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
            pass
        ##########################################
    context = {
        "services": services,
        "projects": projects,
        "experts": experts,
        "partners": partners,
        'news': news,
        'form': form,
    }
    return render(request, "home/index.html", context)