from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'profile_photo', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile_photo',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('profile_photo',)}),
    )

# Register CustomUser with CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)

# Register Book normally
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('author',)

admin.site.register(Book, BookAdmin)
