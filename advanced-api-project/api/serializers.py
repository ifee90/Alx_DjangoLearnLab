"""
serializers.py
---------------
This module defines serializers for the Author and Book models.
Serializers handle the conversion of model instances to JSON and
validate input data for creating/updating records.
"""

from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    - Serializes all fields of a Book (title, publication_year, author).
    - Includes custom validation to prevent a future publication year.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Ensure the publication year is not set in the future.
        """
        from datetime import datetime
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    - Includes the author's id and name.
    - Adds a nested list of the author's books using BookSerializer.
    """
    # 'books' comes from the related_name="books" in the Book model's ForeignKey
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
