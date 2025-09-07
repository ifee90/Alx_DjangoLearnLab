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
    change_book,  # ✅ matches views.py
    delete_book,
)

urlpatterns = [
    # Existing routes
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based routes
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    # Permission-based routes for Book management
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:book_id>/', change_book, name='edit_book'),  # ✅ now points to change_book
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
]
