from django.urls import path
from . import views
from django.contrib.auth.views import (PasswordResetView,
                                       PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("signup/", views.signUpPage, name="signup"),
    path("logout/", views.logoutUser, name="logout"),
    # path("forgot-password/", views.forgotPassword, name="forgot-password"),
    path("reset_password/", PasswordResetView.as_view(
        template_name='authenticate/forgot-password.html'), name="reset_password"),

    path("reset-password-sent/", PasswordResetDoneView.as_view(
        template_name='authenticate/reset-password-sent.html'), name="password_reset_done"),

    path("reset/<uidb64>/<token>", PasswordResetConfirmView.as_view(
        template_name='authenticate/reset.html'), name="password_reset_confirm"),

    path("reset/done/", PasswordResetCompleteView.as_view(template_name='authenticate/password-reset-complete.html'),
         name="password_reset_complete"),

]
