from django.http.response import HttpResponseRedirect
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
        news_obj = News.objects.values('title', 'date') # .order_by('-date')
        comment_form = CommentForm()
        num_of_comments = comments.count()

        # pagination 
        paginator = Paginator(news_obj, 1)
        page_obj = paginator.get_page(id) # id  = page number
        # get the next and previos page titles by use of tenary operator
        next_page_title = news_obj[page_obj.next_page_number()-1]['title'] if page_obj.has_next() else False
        previous_page_title = news_obj[page_obj.previous_page_number()-1]['title']  if page_obj.has_previous() else False

        # pagination for comments
        com_paginator = Paginator(comments, 3)
        page_num = request.GET.get('comment')
        com_odj = com_paginator.get_page(page_num)


        context = {
            'news': news,
            'comments': com_odj,
            'page_obj': page_obj,
            'next_page_title': next_page_title,
            'previous_page_title': previous_page_title,
            'comment_form': comment_form,
            'num_of_comments': num_of_comments,
        }
        return render(request, 'news/news_detail.html', context)

    def post(self, request, id):
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment(
                name = form.cleaned_data['name'],
                message = form.cleaned_data['message'],
                news_id = form.cleaned_data['news_id'],
            )
            comment.save()
            
            return HttpResponseRedirect(f"/news/detail/{id}")
        else:
            form = CommentForm()
