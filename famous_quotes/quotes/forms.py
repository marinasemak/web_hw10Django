from django.forms import ModelForm, CharField, TextInput, DateField, DateInput, Textarea
from datetime import date

from .models import Author, Quote

class AddAuthorForm(ModelForm):
    fullname = CharField(max_length=120, required=True, widget=TextInput(attrs={"class": "form-control"}))
    born_date = DateField(widget=DateInput(attrs={"class": "form-control", "placeholder": "yyyy-mm-dd"}))
    born_location = CharField(max_length=150, widget=TextInput(attrs={"class": "form-control"}))
    description = CharField(widget=Textarea(attrs={"class": "form-control"}))
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

class AddQuoteForm(ModelForm):
    # quote = CharField(required=True, widget=TextInput(attrs={"class": "form-control"}))
    # author = DateField(widget=DateInput(attrs={"class": "form-control"}))
    # tags = CharField(widget=TextInput(attrs={"class": "form-control"}))
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']

