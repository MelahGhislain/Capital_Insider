from django.shortcuts import render
from about.models import AboutUs, Expert

# Create your views here.

def homePage(request):
    return render(request, "home/index.html")