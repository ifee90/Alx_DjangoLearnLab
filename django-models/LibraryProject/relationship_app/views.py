from django.shortcuts import render
# from django.views.generic import DetailView
from .models import Library, Book
# from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm # A built-in form for creating new users.
from django.shortcuts import render # Used to return an HTML response with a template.
from django.contrib.auth.decorators import user_passes_test # A decorator that restricts access to views based on a custom test function.
from django.contrib.auth.decorators import permission_required # A decorator that restricts access to views based on user permissions.



# Create your views here.

# Function-based View to display list of books
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view that displays details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Register view
class RegisterView(CreateView):
    form_class = UserCreationForm
    # If this is a function based view it would be 
    # form = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'


# Role-checking functions
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

# Role protected views using user_passes_test decorator
# Admin
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# @permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    pass
# @permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book(request):
    pass
# @permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request):
    pass


