from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create authors
        self.author = Author.objects.create(name="Test Author")
        self.other_author = Author.objects.create(name="Other Author")

        # Create a book
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )

    def test_create_book(self):
        url = "/api/books/create/"
        data = {"title": "New Book", "publication_year": 2021, "author": self.author.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        url = f"/api/books/{self.book.id}/update/"
        data = {"title": "Updated Book", "publication_year": 2022, "author": self.author.id}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        url = f"/api/books/{self.book.id}/delete/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_unauthorized_update(self):
        url = f"/api/books/{self.book.id}/update/"
        data = {"title": "Hack Update", "publication_year": 2030, "author": self.other_author.id}
        response = self.client.put(url, data, format="json")
        self.assertIn(response.status_code, [status.HTTP_400_BAD_REQUEST, status.HTTP_403_FORBIDDEN])

    def test_unauthorized_delete(self):
        url = f"/api/books/{self.book.id}/delete/"
        response = self.client.delete(url)
        self.assertIn(response.status_code, [status.HTTP_204_NO_CONTENT, status.HTTP_403_FORBIDDEN])

