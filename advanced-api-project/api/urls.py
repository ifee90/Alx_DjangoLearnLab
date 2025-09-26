"""
api/urls.py

This module defines all API endpoints for the `advanced_api_project`.

- Author endpoints use a DRF Router + ViewSet (all CRUD in one).
- Book endpoints use DRF generic views for fine-grained control over CRUD operations.

Each URL pattern is documented for clarity.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AuthorViewSet,
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

# ----------------------------
# Router setup for Author endpoints
# ----------------------------
# Using DefaultRouter to automatically generate routes for AuthorViewSet.
# Provides: /authors/ (list + create) and /authors/{id}/ (retrieve, update, delete).
router = DefaultRouter()
router.register(r'authors', AuthorViewSet)

# ----------------------------
# URL patterns for API endpoints
# ----------------------------
urlpatterns = [
    # Author endpoints (ViewSet-based)
    path('', include(router.urls)),  

    # Book endpoints (Generic Views-based)
    path("books-generic/", BookListView.as_view(), name="book-list"),  
    path("books-generic/<int:pk>/", BookDetailView.as_view(), name="book-detail"),  
    path("books-generic/create/", BookCreateView.as_view(), name="book-create"),  
    path("books-generic/<int:pk>/update/", BookUpdateView.as_view(), name="book-update"),  
    path("books-generic/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),  
]

