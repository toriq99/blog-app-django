from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views import View
from django.urls import reverse

from datetime import date
from .models import Post, Author, Tag, Comment
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


class SinglePostView(View):
    def is_saved_for_later(self, request, post_id):
        stored_posts = request.session.get("stored_posts")  # get session for read later

        if stored_posts is None:
            is_saved_for_later = False
        else:
            is_saved_for_later = post_id in stored_posts

        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)                  # get by slug

        context = {                                         # context untuk parsing ke view
            "post": post,
            "post_tag": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_saved_for_later(request, post.id)
        }
        return render(request, "blog/posts-details.html", context)      # return context disini

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)  
        
        # if the form is valid
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)   # save manually because in form we exclude "post"
            comment.post = post                         # fill post column ex:"mountain-hiking"
            comment.save()

            return HttpResponseRedirect(reverse("posts-detail-page", args=[slug]))

        # if the form unvalid      
        context = {
            "post": post,
            "post_tag": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_saved_for_later(request, post.id)

        }
        return render(request, "blog/posts-details.html", context)

class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)     # fetch post based on id in stored_post 
            context["posts"] = posts
            context["has_posts"] = True
        
        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []
        
        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)                    # (klik) jika belum ada di read later, maka append
        else:
            stored_posts.remove(post_id)                    # (klik) jika sudah ada di read later, maka remove
        
        request.session["stored_posts"] = stored_posts      # saving to session

        return HttpResponseRedirect("/blog")