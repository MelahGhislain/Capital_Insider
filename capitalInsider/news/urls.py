from django.urls import path
from . import views


urlpatterns  = [
    path('',views.NewsView.as_view() , name = 'news'),
    path('detail/<int:id>/',views.NewsDetailView.as_view() , name = 'news-detail'),
]