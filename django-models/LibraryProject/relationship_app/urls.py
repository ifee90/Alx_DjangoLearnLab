from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    list_books,
    LibraryDetailView,
    register,
    admin_view,
    librarian_view,
    member_view,
    add_book,
    change_book,  # ensure this matches your view name
    delete_book,
)

urlpatterns = [
    # Book list and library detail
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based views
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    # Permission-based book management
    path('add_book/', add_book, name='add_book'),           # ✅ must be exactly "add_book/"
    path('edit_book/<int:book_id>/', change_book, name='edit_book'),  # ✅ must be exactly "edit_book/"
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
]
