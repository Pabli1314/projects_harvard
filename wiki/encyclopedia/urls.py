from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.results, name="results"),
    path("wiki/", views.searchEncyclopedia, name="search"),
]
