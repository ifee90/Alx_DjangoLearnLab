from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    Provides list, create, retrieve, update, partial_update and destroy actions
    for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can access this viewset
    permission_classes = [permissions.IsAuthenticated]
