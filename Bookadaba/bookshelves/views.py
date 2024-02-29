from django.shortcuts import render
from django.http import HttpResponse
from .models import bookshelf 

# Create your views here.
def index(request):

    context={
        "bookshelves": bookshelf.objects.all()
    }

    return render(request, "bookshelves/index.html", context)
