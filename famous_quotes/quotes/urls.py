from django.urls import path

from .views import QuotesListView, AuthorDetailView

app_name = "quotes"

urlpatterns = [
    path("", QuotesListView.as_view(), name="home"),  # quotes:home
    path("author/<slug:slug>/", AuthorDetailView.as_view(), name="author"),  # quotes:author
]

