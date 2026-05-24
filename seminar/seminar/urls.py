from django.urls import path


from . import views

urlpatterns = [
    path("", views.book_list, name="book_list"),

    path("book/add/", views.book_add, name="book_add"),
    path("book/<int:pk>/", views.book_detail, name="book_detail"),
    path("book/<int:pk>/edit/", views.book_edit, name="book_edit"),
    path("book/<int:pk>/delete/", views.book_delete, name="book_delete"),
    path("book/<int:pk>/return/", views.return_book, name="return_book"),
    path("book/<int:pk>/rent/", views.rent_book, name="rent_book"),

    path("statistics/", views.statistics, name="statistics"),

    path("signup/", views.signup, name="signup"),
]
