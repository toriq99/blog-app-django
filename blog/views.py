from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from datetime import date

from .models import *

# Create your views here.

def index(request):
    latest_post = Post.objects.all().order_by("-date")[:3]
    return render(request, 'blog/index.html',{
        "post": latest_post,
    })

def posts(request):
    post_data = Post.objects.all()
    return render(request, 'blog/all-posts.html', {
        "all_posts": post_data,
    })

def posts_details(request, slug):
    """
    # sudah tidak perlu
    identifier = next(items for items in post_data if items['slug'] == slug)  # pointer untuk memilih post berdasarkan slug
    """
    identifier = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/posts-details.html', {
        "post": identifier,
    })