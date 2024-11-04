from django.urls import path

from .views import QuotesListView

app_name = "quotes"

urlpatterns = [
    path("", QuotesListView.as_view(), name="home"),  # quotes:home
    # path("author/", views.author, name="author"),  # quotes:author
]
