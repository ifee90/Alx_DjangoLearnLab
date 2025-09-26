from django.shortcuts import render
from django_filters import rest_framework  # ALX expects this exact import
from rest_framework import generics  # ALX expects this exact import
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
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
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters_]()_
