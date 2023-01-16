from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def posts(request):
    return HttpResponse("post url success")

def posts_details(request):
    return HttpResponse("spesific post url success")