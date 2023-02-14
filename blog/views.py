from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from datetime import date
from .models import *
from .forms import CommentForm

# Create your views here.

class IndexView(ListView):              # Rubah index view kedalam ListView
    model = Post
    template_name = "blog/index.html"
    ordering = ["-date"]                # menentukan order by
    context_object_name = "post"        # merubah object data di view menjadi posts

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class AllPostView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    ordering = ["-date"]
    context_object_name = "all_posts"

# post detail using class based
class SinglePostView(DetailView):
    model = Post
    template_name = "blog/posts-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tag"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context
    

"""
def posts_details(request, slug):
  
    # sudah tidak perlu
    # identifier = next(items for items in post_data if items['slug'] == slug)  # pointer untuk memilih post berdasarkan slug

    identifier = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/posts-details.html', {
        "post": identifier,
    })

"""
