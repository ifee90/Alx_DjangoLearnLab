from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


# -----------------------------
# Post ViewSet (CRUD)
# -----------------------------
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Return posts in reverse chronological order
        return Post.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# -----------------------------
# Comment ViewSet (CRUD)
# -----------------------------
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# -----------------------------
# Feed View — show posts from followed users
# -----------------------------
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_feed(request):
    """
    Returns a list of posts created by users that the current user follows.
    Ordered from newest to oldest.
    """
    user = request.user
    following_users = user.following.all()  # Users that the current user follows
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
