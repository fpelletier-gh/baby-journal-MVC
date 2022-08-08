"""Defines URL patterns for baby_logs"""
from django.urls import path, include
from django.contrib.auth import views
from .forms import LoginForm

from . import views as users_views

app_name = "users"
urlpatterns = [
    # Default auth url
    path(
        "login/",
        views.LoginView.as_view(
            template_name="registration/login.html", authentication_form=LoginForm
        ),
        name="login",
    ),
    path("register/", users_views.register, name="register"),
    path("", include("django.contrib.auth.urls")),
]
