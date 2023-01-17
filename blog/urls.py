from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home-page"),
    path('posts/', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.posts_details, name='posts-detail-page') # /posts/my-first-page
]
