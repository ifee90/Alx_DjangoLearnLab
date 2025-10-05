from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# -------------------------
# Tag Model
# -------------------------
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# -------------------------
# Post Model
# -------------------------
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)  # Added tagging support
    published_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Track edits

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Redirect to the post detail page after creation or update
        return reverse('post-detail', kwargs={'pk': self.pk})


# -------------------------
# Comment Model
# -------------------------
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

    def get_absolute_url(self):
        # Redirect back to the post detail page after comment creation or update
        return reverse('post-detail', kwargs={'pk': self.post.pk})
