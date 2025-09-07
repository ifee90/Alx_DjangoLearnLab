from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book, Library

# Function-based view: List all books as plain text
def list_books(request):
    books = Book.objects.all()
    response_text = ""
    for book in books:
        response_text += f"{book.title} by {book.author.name}\n"
    # Remove the last newline to match ALX exact check
    response_text = response_text.rstrip("\n")
    return HttpResponse(response_text, content_type="text/plain")

# Class-based view: Show details of a specific library (HTML template)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
