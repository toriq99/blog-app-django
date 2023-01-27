from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.city}"

    class Meta:
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.fullname()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    authors = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    published_country = models.ManyToManyField(Country)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    # make object in terminal more readable
    def __str__(self):
        return f"{self.title} ({self.rating})"