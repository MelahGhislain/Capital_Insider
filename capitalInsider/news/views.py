from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
# from django.views.generic import ListView
from .models import News, Comment
from about.models import AboutUs

# Create your views here.
class NewsView(View):
    def get(self, request):
        news = News.objects.all().order_by('-date')
        about = AboutUs.objects.first()
        # get the date
        archive = map(lambda news: {
            "date": news.date
        } , News.objects.all())

        # pagination
        paginator = Paginator(news, 4)
        page_number = request.GET.get('page')
        page_odj = paginator.get_page(page_number)



        context = {
            'news': page_odj,
            'about': about,
            'archive': archive,
        }
        return render(request, 'news/index.html', context)

class NewsDetailView(View):
    def get(self, request, id):
        news = News.objects.get(id=id)
        context = {
            'news': news,
        }
        return render(request, 'news/news_detail.html', context)
