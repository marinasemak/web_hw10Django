from django.shortcuts import render
from django.views.generic import ListView

from .models import Quote

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

