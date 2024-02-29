from django.shortcuts import render
from django.http import HttpResponse
from .models import bookshelf, Book

# Create your views here.
def index(request):
    
    all_bookshelves = bookshelf.objects.all()
    all_books = Book.objects.all()

    context = {
        "bookshelves": all_bookshelves,
        "books": all_books,
    }

    return render(request, "bookshelves/index.html", context)
