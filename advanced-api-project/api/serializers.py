from rest_framework import serializers
from .models import Author, Book

# ----------------------------
# BookSerializer
# ----------------------------
# This serializer is responsible for handling the Book model.
# It serializes all fields of the Book (title, publication_year, author).
# It also includes a custom validation to prevent using a future year.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation method for publication_year
    def validate_publication_year(self, value):
        from datetime import datetime
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# ----------------------------
# AuthorSerializer
# ----------------------------
# This serializer is responsible for handling the Author model.
# It includes the author's name and a nested list of their books.
# The 'books' field uses BookSerializer to serialize related Book objects.
class AuthorSerializer(serializers.ModelSerializer):
    # 'related_name="books"' from models lets us access all books for an author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
