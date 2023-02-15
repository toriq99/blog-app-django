from django.contrib import admin
from .models import Post, Author, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'date',)
    list_filter = ('date', 'author',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)