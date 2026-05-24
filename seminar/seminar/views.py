from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Book
from django.db import models

def book_list(request):
    books = Book.objects.all()
    query = request.GET.get("q")
    author = request.GET.get("author")

    if query:
        books = books.filter(title__icontains=query)
    if author:
        books = books.filter(
            models.Q(authors__first_name__icontains=author) |
            models.Q(authors__last_name__icontains=author)
        )

    return render(request, "seminar/book_list.html", {"books": books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "seminar/book_detail.html", {"book": book})

