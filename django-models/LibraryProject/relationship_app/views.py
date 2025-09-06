from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book, Library

# Function-based view: List all books as plain text (ALX requirement)
def list_books(request):
    books = Book.objects.all()
    # Create a simple text list: "Title by Author"
    output = "\n".join(f"{book.title} by {book.author.name}" for book in books)
    return HttpResponse(output)

# Class-based view: Show details of a specific library (HTML template)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
