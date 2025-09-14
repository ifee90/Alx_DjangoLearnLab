from django.db import models
from django.contrib.auth.models import AbstractUser

# ✅ Custom user model
class CustomUser(AbstractUser):
    pass

# ✅ Library model
class Library(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

# ✅ Book model (linked to Library)
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)

    # ✅ ALX task requirements
    can_create = True
    can_delete = True

    def __str__(self):
        return f"{self.title} by {self.author}"



