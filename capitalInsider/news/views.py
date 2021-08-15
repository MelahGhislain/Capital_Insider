from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
# from django.views.generic import ListView
from .models import News, Comment
from about.models import AboutUs
from .forms import CommentForm

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
        comments = news.comments.all()
        print(comments)
        news_odj = News.objects.all() # get news except for current news
        comment_form = CommentForm()
        context = {
            'news': news,
            'news_odj': news_odj,
            'comment_form': comment_form,
        }
        return render(request, 'news/news_detail.html', context)

    def post(self, request):
        form = CommentForm(request.POST)

        if form.is_valid():
            pass
            # form.save()
