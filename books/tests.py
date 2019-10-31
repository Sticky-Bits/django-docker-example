from django.test import TestCase
from books.models import Author, Book


class BookTests(TestCase):
    def test_books_are_books(self):
        author = Author.objects.create(name='My Author')
        book = Book.objects.create(name='My Book Name', author=author)
        self.assertEqual(author.name, book.author.name)
