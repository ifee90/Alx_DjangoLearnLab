# api/urls.py
from django.urls import path, include
from .views import BookListCreateView, BookRetrieveUpdateDeleteView, AuthorViewSet
from rest_framework.routers import DefaultRouter

# Author router
router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-detail'),
    path('', include(router.urls)),
]
