# api/test_views.py

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Book, Author

class BookAPITests(APITestCase):

    def setUp(self):
        # Create test user and log in
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Create test authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create test books
        self.book1 = Book.objects.create(title="Book One", publication_year=2000, author=self.author1)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2005, author=self.author2)

    def test_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Book One', str(response.data))
        self.assertIn('Book Two', str(response.data))

    def test_book_create(self):
        url = reverse('book-list')
        data = {
            'title': 'Book Three',
            'publication_year': 2010,
            'author': self.author1.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Book Three')

    def test_book_update(self):
        url = reverse('book-detail', args=[self.book1.id])
        data = {
            'title': 'Updated Book One',
            'publication_year': 2001,
            'author': self.author1.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Book One')

    def test_book_delete(self):
        url = reverse('book-detail', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
