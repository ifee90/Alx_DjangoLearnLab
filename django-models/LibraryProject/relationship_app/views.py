from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library

# Function-based view: HTML template list of books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: Library details (HTML template)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # ensure this file exists in templates/
    context_object_name = 'library'

