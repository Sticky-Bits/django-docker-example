from django.db import models


class Book(models.Model):
    name = models.TextField(max_length=200)
    author = models.ForeignKey('books.Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.TextField(max_length=200)

    def __str__(self):
        return self.name
