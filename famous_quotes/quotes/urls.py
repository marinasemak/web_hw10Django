from django.urls import path

from .views import QuotesListView, AuthorDetailView, AuthorCreateView, QuoteCreateView

app_name = "quotes"

urlpatterns = [
    path("", QuotesListView.as_view(), name="home"),  # quotes:home
    path(
        "author/<slug:slug>/", AuthorDetailView.as_view(), name="author"
    ),  # quotes:author
    path(
        "add-author", AuthorCreateView.as_view(), name="add_author"
    ),  # quotes:add_author
    path("add-quote", QuoteCreateView.as_view(), name="add_quote"),  # quotes:add_quote
]
