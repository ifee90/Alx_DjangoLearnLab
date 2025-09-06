from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Book, Library

# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

from django.views.generic.detail import DetailView

# Class-based view: Show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
