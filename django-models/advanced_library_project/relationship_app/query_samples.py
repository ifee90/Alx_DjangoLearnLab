import os
import sys
import django

# 🔑 Step 1: Find the outer project folder (where manage.py is)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 🔑 Step 2: Add it to Python's path
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# 🔑 Step 3: Point Django to the inner LibraryProject/settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

# 🔑 Step 4: Setup Django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian



def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with the name {author_name}")


def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in library '{library_name}':")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian for '{library_name}': {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library_name}'")


    try:
        # Reverse OneToOne access: Library -> Librarian
        librarian = library.librarian
        print(f"Librarian for '{library.name}': {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to '{library.name}'")

if __name__ == "__main__":
    # Change the names to match data in your database
    query_books_by_author("John Doe")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
