from django.db import models
from django.conf import settings  # <- important for custom user reference

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # <- points to users.CustomUser
        on_delete=models.CASCADE,
        related_name='books_added'
    )

    def __str__(self):
        return self.title


