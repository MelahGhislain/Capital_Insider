from django.urls import path
from  . import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("signup/", views.signUpPage, name="signup"),
    path("logout/", views.logoutUser, name="logout"),
    path("forgot-password/", views.forgotPassword, name="forgot-password"),
]