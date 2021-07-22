from django.shortcuts import render
from .models import AboutUs, Expert

# Create your views here.
def aboutPage(request):
    about = AboutUs.objects.last()
    experts = Expert.objects.all()
    return render(request, "about/index.html",{
                    "about": about,
                    "experts": experts
                })