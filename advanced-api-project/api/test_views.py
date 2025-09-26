# api/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book

class BookAPITests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Chinua Achebe")
        self.book1 = Book.objects.create(
            title="Things Fall Apart", publication_year=1958, author=self.author
        )
        self.book2 = Book.objects.create(
            title="No Longer at Ease", publication_year=1980, author=self.author
        )

    def test_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('title' in response.data[0])
        self.assertTrue('publication_year' in response.data[0])
        self.assertTrue('author' in response.data[0])

    def test_book_create(self):
        url = reverse('book-list')
        # Authenticate a dummy user for POST
        self.client.force_authenticate(user=None)
        data = {
            "title": "Arrow of God",
            "publication_year": 1964,
            "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_book_update(self):
        url = reverse('book-detail', args=[self.book1.id])
        self.client.force_authenticate(user=None)
        data = {"title": "Things Fall Apart - Updated"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_delete(self):
        url = reverse('book-detail', args=[self.book2.id])
        self.client.force_authenticate(user=None)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
