from django.db import models

# Create your models here.


class Author(models.Model):
    fullname = models.CharField(max_length=120, unique=True)
    born_date = models.DateField()
    born_location = models.CharField(max_length=150)
    description = models.TextField(blank=True)


class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

class QuoteTag(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
