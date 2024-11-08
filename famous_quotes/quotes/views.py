from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Quote, Author

# Create your views here.


# def index(request):
#     quotes = Quote.objects.all()
#     return render(
#         request, template_name="quotes/index.html", context={"quotes": quotes}
#     )


def author(request):
    return render(request, template_name="quotes/author.html", context={})

class QuotesListView(ListView):
    model = Quote
    template_name = "quotes/index.html"
    context_object_name = 'quotes'

    # def get_queryset(self):
    #     return Quote.objects.select_related('author').all()

class AuthorDetailView(DetailView):
    model = Author
    template_name = "quotes/author.html"
    context_object_name = 'author'

