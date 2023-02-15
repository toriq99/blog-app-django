from django.contrib import admin
from .models import Book, Author, Address, Country

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('authors', 'rating',)
    list_display = ("title", "authors",)

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
