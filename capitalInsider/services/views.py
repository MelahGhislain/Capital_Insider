from django.shortcuts import render
from .models import Services, Brochures
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login')
def servicePage(request):
    services = Services.objects.all()
    
    return render(request, 'services/index.html',{
        "services_data": services,
    })


# @login_required(login_url='login')
def serviceDetail(request, id):
    bronchures = Brochures.objects.first()
    services = Services.objects.all()
    service_data = Services.objects.get(id=id)
    service_titles = map(lambda data: {"title": data.title, "id": data.id} , services) 
    return render(request, 'services/service_detail.html',
                {
                    "service": service_data, 
                    "service_titles": service_titles,
                    'bronchures': bronchures,
                 })

