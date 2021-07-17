from django.shortcuts import render

# Create your views here.
def servicePage(request):

    return render(request, 'services/index.html')

