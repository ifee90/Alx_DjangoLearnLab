from .models import Library
from .models import Book
from django.shortcuts import render
from django.views.generic.detail import DetailView

# Function-based view: HTML template list of books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: Library details (HTML template)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
