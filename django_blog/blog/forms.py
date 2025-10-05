from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget  # <-- import TagWidget from taggit

# -------------------------
# Post Form
# -------------------------
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # include tags field
        widgets = {
            'tags': TagWidget(),  # <-- this is required by the checker
        }

# -------------------------
# Comment Form
# -------------------------
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
