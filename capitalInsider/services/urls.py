from django.urls import path
from . import views

urlpatterns = [
    path("", views.servicePage, name="services"),
    path("detail/", views.servicePage, name="service-detail"),
]
