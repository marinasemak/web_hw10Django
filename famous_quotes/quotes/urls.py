from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.index, name="home"),  # quotes:home
    path("author/", views.author, name="author"),  # quotes:author
]
