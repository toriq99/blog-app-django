from django.shortcuts import render
from .models import Book

# Create your views here.

def index(request):
    book_model = Book.objects.all()
    return render(request, "book_outlet/index.html", {
        'books': book_model,
    })

def book_detail(request, id):
    selected_book = Book.objects.get(pk = id)
    return render(request, "book_outlet/book_detail.html", {
        'book': selected_book
    })