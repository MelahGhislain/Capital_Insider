from django.shortcuts import render
from django.views import View
# from django.views.generic import ListView
from .models import News, Comment

# Create your views here.
class NewsView(View):
    def get(self, request):
        news = News.objects.all()
        context = {
            'news': news,
        }
        return render(request, 'news/index.html', context)

class NewsDetailView(View):
    def get(self, request, id):
        return render(request, 'news/news_detail.html')
