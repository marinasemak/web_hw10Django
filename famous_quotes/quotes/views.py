from django.shortcuts import render

from famous_quotes.quotes.models import Quote

# Create your views here.


def index(request):
    quotes = Quote.objects.all()
    return render(
        request, template_name="quotes/index.html", context={"msg": "Hello world"}
    )


def author(request):
    return render(request, template_name="quotes/author.html", context={})
