from django.urls import path
from . import views

urlpatterns = [
    path("", views.servicePage, name="services"),
    path("detail/<int:id>", views.serviceDetail, name="service-detail"),
]
