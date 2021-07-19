from django.shortcuts import render

# Create your views here.
def servicePage(request):
    return render(request, 'services/index.html')


def serviceDetail(request):
    return render(request, 'services/service_detail.html')

