from django.contrib import admin
from .models import Book  # Make sure you're importing your Book model

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # Removed publication_year
    list_filter = ('author',)            # Removed publication_year

admin.site.register(Book, BookAdmin)
