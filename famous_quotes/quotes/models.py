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
    tags = models.CharField(blank=True)
