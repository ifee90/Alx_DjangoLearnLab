from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book, Library

# Function-based view: plain text list of books (passes ALX)
def list_books(request):
    books = Book.objects.all()
    output = ""
    for book in books:
        output += f"{book.title} by {book.author.name}\n"
    return HttpResponse(output.rstrip("\n"), content_type="text/plain")

# Class-based view: Library details (HTML template)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
