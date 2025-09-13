from django.contrib import admin

# relationship_app has no local models to register.
# The Author, Library, Book and CustomUser models live in the 'bookshelf' app
# and are already (or should be) registered in bookshelf/admin.py.
# Keep this file minimal to avoid import errors.

# If you later add models to relationship_app, register them here, e.g.:
# from .models import SomeModel
# admin.site.register(SomeModel)
