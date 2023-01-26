from django.shortcuts import render
from .models import Book
from django.db.models import Avg

# Create your views here.

def index(request):
    book_model = Book.objects.all().order_by("-rating")
    num_books = book_model.count()
    avg_rating = book_model.aggregate(Avg('rating')) # use rating__avg in templates

    return render(request, "book_outlet/index.html", {
        'books': book_model,
        'books_total': num_books,
        'average_rating': avg_rating
    })

def book_detail(request, slug):
    # bisa menggunakan get_object_or_404
    """
    contoh :
    book = get_object_or_404(Book, slug = slug)

    """
    selected_book = Book.objects.get(slug = slug)
    return render(request, "book_outlet/book_detail.html", {
        'book': selected_book
    })