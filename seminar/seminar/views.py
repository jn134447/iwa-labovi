from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.db import models
from django.db.models import Count
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book, Rental, Author
from .forms import BookForm


def book_list(request):
    books = Book.objects.all()
    query = request.GET.get("title")
    author = request.GET.get("author")

    if query:
        books = books.filter(title__icontains=query)
    if author:
        for word in author.split():
            books = books.filter(
                models.Q(authors__first_name__icontains=word)
                | models.Q(authors__last_name__icontains=word)
            )

    return render(request, "seminar/book_list.html", {"books": books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    user_has_rented = False
    if request.user.is_authenticated:
        user_has_rented = Rental.objects.filter(book=book, user=request.user).exists()
    return render(
        request,
        "seminar/book_detail.html",
        {
            "book": book,
            "user_has_rented": user_has_rented,
        },
    )


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


# employee stuff


def is_employee(user):
    return user.groups.filter(name="Employees").exists()

def is_staff_or_employee(user):
    return user.is_staff or is_employee(user)


@login_required
@user_passes_test(is_staff_or_employee)
def statistics(request):
    total_rentals = Rental.objects.count()
    top_books = Book.objects.annotate(rental_count=Count("rental")).order_by(
        "-rental_count"
    )[:5]
    top_authors = Author.objects.annotate(rental_count=Count("book__rental")).order_by(
        "-rental_count"
    )[:5]
    recent_rentals = Rental.objects.order_by("-rented_at")[:10]

    return render(
        request,
        "seminar/statistics.html",
        {
            "total_rentals": total_rentals,
            "top_books": top_books,
            "top_authors": top_authors,
            "recent_rentals": recent_rentals,
        },
    )


# renting stuff


@login_required
def rent_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    Rental.objects.create(book=book, user=request.user)
    return redirect("book_detail", pk=pk)


@login_required
def return_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    Rental.objects.filter(book=book, user=request.user).delete()
    return redirect("book_detail", pk=pk)
