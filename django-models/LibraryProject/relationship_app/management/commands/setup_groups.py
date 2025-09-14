#!/usr/bin/env python3
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_features_and_security.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book
from django.contrib.contenttypes.models import ContentType

# Define groups
groups_permissions = {
    "Editors": ["can_add_book", "can_change_book", "can_delete_book"],
    "Viewers": ["can_view_book"],
    "Admins": ["can_add_book", "can_change_book", "can_delete_book", "can_view_book"],
}

# Ensure the permissions exist
content_type = ContentType.objects.get_for_model(Book)

# Create permissions if they don't exist
permissions_mapping = {
    "can_add_book": Permission.objects.get_or_create(codename="can_add_book", name="Can add book", content_type=content_type)[0],
    "can_change_book": Permission.objects.get_or_create(codename="can_change_book", name="Can change book", content_type=content_type)[0],
    "can_delete_book": Permission.objects.get_or_create(codename="can_delete_book", name="Can delete book", content_type=content_type)[0],
    "can_view_book": Permission.objects.get_or_create(codename="can_view_book", name="Can view book", content_type=content_type)[0],
}

# Create groups and assign permissions
for group_name, perms in groups_permissions.items():
    group, created = Group.objects.get_or_create(name=group_name)
    for perm in perms:
        group.permissions.add(permissions_mapping[perm])
    print(f"Group '{group_name}' created with permissions: {', '.join(perms)}")

print("Groups and permissions setup complete!")
