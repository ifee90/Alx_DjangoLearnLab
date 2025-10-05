from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment  # import Post and Comment models

# Custom user registration form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

# Post form for creating and updating blog posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # author will be set automatically in the view

# Comment form for creating and updating comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Only content; author and post set in the view
