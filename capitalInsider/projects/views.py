from django.shortcuts import render
from .models import Projects
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login')
def projectPage(request):
    projects = Projects.objects.all().order_by("-year_completed")
    # will be use to filter  the projects to get mainImage, title, categoty
    project_data = map(lambda x: {"id": x.id,
                    "category": x.category,
                    "title": x.title,
                    "main_image": x.main_image
                     }, projects)
    project_categories = map(lambda x: {"category": x.category,}, projects)

    return render(request, "projects/index.html", {
        "project_data": project_data,
        "project_categories": project_categories,
        })

# @login_required(login_url='login')
def projectDetail(request, id):
    project = Projects.objects.get(pk=id)
    return render(request, 'projects/project_detail.html', {"project": project})
