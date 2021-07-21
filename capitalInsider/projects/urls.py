from django.urls import path
from . import views

urlpatterns = [
    path("", views.projectPage, name="projects"),
    path("detail/<int:id>/", views.projectDetail, name="project-detail"),
]
