from django.shortcuts import render

# Create your views here.
def projectPage(request):
    return render(request, "projects/index.html")

def projectDetail(request):
    return render(request, 'projects/project_detail.html')
