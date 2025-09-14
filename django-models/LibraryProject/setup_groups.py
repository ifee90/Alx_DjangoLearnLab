import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

def create_groups():
    # Create Librarian group
    librarian_group, created = Group.objects.get_or_create(name="Librarian")

    # Give Librarian all permissions for Book model
    content_type = ContentType.objects.get_for_model(Book)
    permissions = Permission.objects.filter(content_type=content_type)
    librarian_group.permissions.set(permissions)

    # Create Member group
    Group.objects.get_or_create(name="Member")

    print("Groups created successfully!")

if __name__ == "__main__":
    create_groups()

