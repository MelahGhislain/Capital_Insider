from django.shortcuts import render
from .models import Services, Brochures

# Create your views here.
def servicePage(request):
    services = Services.objects.all()
    services_data = map(lambda data: {
        "id": data.id,
        "image": data.service_image ,
        "title": data.title,
        "description": data.description[:100],
    },services)
    return render(request, 'services/index.html',{
        "services_data": services_data,
    })


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

