from django.urls import path
from . import views

urlpatterns = [
    path("", views.projectPage, name="projects"),
    # path("detail/", views.projectDetail, name="project-detail"),
]
