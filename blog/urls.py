from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='blog'),
    path('posts/', views.AllPostView.as_view(), name='posts-page'),
    path('posts/<slug:slug>', views.SinglePostView.as_view(), name='posts-detail-page') # /posts/my-first-page
]
