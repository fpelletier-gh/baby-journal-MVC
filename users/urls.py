"""Defines URL patterns for baby_logs"""
from django.urls import path, include

from . import views

app_name = "users"
urlpatterns = [
    # Default auth url
    path("", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
]

