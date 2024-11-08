from django.db import models
from django.urls import reverse

# Create your models here.


class Author(models.Model):
    fullname = models.CharField(max_length=120, unique=True)
    born_date = models.DateField()
    born_location = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    # def get_absolute_url(self):
    #     formatted_name = self.fullname.replace(" ", "-")
    #     return reverse('author', args=[formatted_name])

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tag, related_name='quotes')


