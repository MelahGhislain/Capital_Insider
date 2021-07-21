from django.shortcuts import render
from .models import Projects

# Create your views here.
def projectPage(request):
    projects = Projects.objects.all().order_by("-year_completed")
    # will be use to filter  the projects to get mainImage, title, categoty
    project_data = map(lambda x: {"category": x.category,
                    "title": x.title,
                    "main_image": x.main_image
                     }, projects)
    project_categories = map(lambda x: {"category": x.category,}, projects)

    return render(request, "projects/index.html", {
        "projects": project_data,
        "project_categories": project_categories,
        })

def projectDetail(request, id):
    pk = str(id)
    project = Projects.objects.all().filter(id=pk)
    return render(request, 'projects/project_detail.html', {"project": project})
