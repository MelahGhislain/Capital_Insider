from django.shortcuts import render
from .models import Projects

# Create your views here.
def projectPage(request):
    projects = Projects.objects.all()# .order_by("-year_completed")
    # will be use to filter  the projects to get mainImage, title, categoty
    # project_data = projects.
    return render(request, "projects/index.html", {"projects": projects})

def projectDetail(request):
    return render(request, 'projects/project_detail.html')
