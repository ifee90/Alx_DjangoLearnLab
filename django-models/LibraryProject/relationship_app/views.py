from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book, Library

# Function-based view: List all books as plain text (ALX requirement)
def list_books(request):
    books = Book.objects.all()
    output_lines = []
    for book in books:
        output_lines.append(f"{book.title} by {book.author.name}")
    output_text = "\n".join(output_lines)
    return HttpResponse(output_text, content_type="text/plain")

# Class-based view: Show details of a specific library (HTML template)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
