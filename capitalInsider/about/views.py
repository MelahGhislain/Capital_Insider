from django.shortcuts import render
from .models import AboutUs, Expert
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def aboutPage(request):
    about = AboutUs.objects.last()
    experts = Expert.objects.all()
    return render(request, "about/index.html",{
                    "about": about,
                    "experts": experts
                })