from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def delete(self, *args, **kwargs):
        for book in self.book_set.all(): # type: ignore
            book.delete()
        return super().delete(*args, **kwargs)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    authors = models.ManyToManyField(Author)
    cover_image = models.ImageField(upload_to="covers/", blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
