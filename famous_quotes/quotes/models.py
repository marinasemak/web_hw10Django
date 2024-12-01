from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Author(models.Model):
    fullname = models.CharField(max_length=120, unique=True)
    born_date = models.DateField()
    born_location = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # formatted_name = self.fullname.replace(" ", "-")
        return reverse("quotes:author", kwargs={"slug": self.slug})


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    tags = models.ManyToManyField(Tag, related_name="quotes")

    def __str__(self):
        return self.tags
