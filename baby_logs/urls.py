"""Defines URL patterns for baby_logs"""
from django.urls import path

from . import views

app_name = "baby_logs"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    path("babies/", views.babies, name="babies"),
    # Detail page for a single baby.
    path("babies/<int:baby_id>/", views.baby, name="baby"),
    # Page for adding a new baby
    path("new_baby/", views.new_baby, name="new_baby"),
    path("delete_baby/<int:baby_id>/", views.delete_baby, name="delete_baby"),
    path("new_post/<int:baby_id>/", views.new_post, name="new_post"),
    path("edit_post/<int:post_id>/", views.edit_post, name="edit_post"),
]
