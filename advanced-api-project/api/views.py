from django.shortcuts import render
from django_filters import rest_framework
from rest_framework import generics, viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# -----------------------------------------
# Author Views
# -----------------------------------------
class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Author objects.

    Features:
    - Provides all CRUD operations (list, retrieve, create, update, delete).
    - Uses AuthorSerializer to serialize data.
    - Anyone can view authors; creating, updating, and deleting requires authentication.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# -----------------------------------------
# Book Views
# -----------------------------------------
# Individual generic views for Book model to demonstrate DRF generics.

class BookListView(generics.ListAPIView):
    """
    List all books (GET request) with advanced query capabilities.

    Features:
    - Filtering: ?title=xxx, ?author=1, ?publication_year=2020
    - Search: ?search=keyword (searches title and author's name)
    - Ordering: ?ordering=title or ?ordering=-publication_year
    - Publicly accessible: no authentication required to view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, search, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']


class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by its ID (GET request).
    - Publicly accessible: anyone can view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    Create a new book (POST request).
    - Only authenticated users can create.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book (PUT/PATCH request).
    - Only authenticated users can update.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book (DELETE request).
    - Only authenticated users can delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
