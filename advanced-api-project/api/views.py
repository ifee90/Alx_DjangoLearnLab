from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# -----------------------------------------
# Author Views
# -----------------------------------------
class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Author objects.

    - Provides all CRUD operations (list, retrieve, create, update, delete)
      without needing to define each view separately.
    - Uses AuthorSerializer to serialize data.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# -----------------------------------------
# Book Views
# -----------------------------------------
# Instead of a ViewSet, we use individual generic views
# to show how DRF generic classes work one by one.


class BookListView(generics.ListAPIView):
    """
    List all books (GET request).
    - Publicly accessible.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # anyone can view


class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by its ID (GET request).
    - Publicly accessible.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    Create a new book (POST request).
    - Only authenticated users can create.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book (PUT/PATCH request).
    - Only authenticated users can update.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book (DELETE request).
    - Only authenticated users can delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
