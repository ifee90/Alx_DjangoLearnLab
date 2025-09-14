from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    list_books,
    add_book,
    change_book,
    delete_book,
)

urlpatterns = [
    # Book management
    path('books/', list_books, name='list_books'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', change_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),

    # Authentication
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]


