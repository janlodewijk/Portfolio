from django.contrib import admin
from .models import bookshelf, Book

# Register your models here.
admin.site.register(bookshelf)
admin.site.register(Book)
