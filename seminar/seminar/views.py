from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Book
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import BookForm

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


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

# admin stuff


def is_admin(user):
    return user.is_staff or user.is_superuser

@login_required
@user_passes_test(is_admin)
def book_add(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "seminar/book_form.html", {"form": form})

@login_required
@user_passes_test(is_admin)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "seminar/book_form.html", {"form": form})

@login_required
@user_passes_test(is_admin)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "seminar/book_confirm_delete.html", {"book": book})