from django.shortcuts import render
from django.views import View
# from django.views.generic import ListView

# Create your views here.
class NewsView(View):
    def get(self, request):
        return render(request, 'news/index.html')

class NewsDetailView(View):
    def get(self, request, id):
        return render(request, 'news/news_detail.html')
