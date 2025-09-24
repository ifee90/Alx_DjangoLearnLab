from django.db import models

class Author(models.Model):
    # Author has only one field: name
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    # Book fields
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    # Relationship: One Author can have many Books
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
