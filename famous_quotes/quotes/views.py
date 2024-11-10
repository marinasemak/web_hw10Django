from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Quote, Author
from .forms import AddAuthorForm, AddQuoteForm

def author(request):
    return render(request, template_name="quotes/author.html", context={})

class QuotesListView(ListView):
    model = Quote
    template_name = "quotes/index.html"
    context_object_name = 'quotes'

    def get_queryset(self):
        return Quote.objects.select_related('author').all()

class AuthorDetailView(DetailView):
    model = Author
    template_name = "quotes/author.html"
    context_object_name = 'author'

class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    template_name = 'quotes/add_author.html'
    form_class = AddAuthorForm
    success_url = reverse_lazy('quotes:home')


class QuoteCreateView(LoginRequiredMixin, CreateView):
    model = Quote
    template_name = 'quotes/add_quote.html'
    form_class = AddQuoteForm
    success_url = reverse_lazy('quotes:home')


