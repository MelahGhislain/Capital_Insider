from django.shortcuts import render
from .models import Services, Brochures
from django.core.paginator import Paginator

# Create your views here.
def servicePage(request):
    services = Services.objects.all()

    paginator = Paginator(services, 3)
    page_number = request.GET.get('page')
    print(page_number)
    print(paginator.get_page(2))
    page_obj = paginator.get_page(1)
    return render(request, 'services/index.html',{
        "services_data": page_obj,
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

