from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification  # For creating notifications


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


# -----------------------------
# Like a Post
# -----------------------------
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    """
    Allows a user to like a post.
    Prevents multiple likes by the same user using get_or_create.
    """
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    like, created = Like.objects.get_or_create(user=user, post=post)
    if not created:
        return Response({'message': 'You have already liked this post.'})

    # Create notification for the post author
    if post.author != user:
        Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb='liked your post',
            target=post
        )

    return Response({'message': 'Post liked successfully.'}, status=status.HTTP_200_OK)


# -----------------------------
# Unlike a Post
# -----------------------------
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    """
    Allows a user to unlike a post they previously liked.
    """
    post = get_object_or_404(Post, pk=pk)
    user = request.user

    like = Like.objects.filter(user=user, post=post).first()
    if not like:
        return Response({'message': 'You have not liked this post.'})

    like.delete()
    return Response({'message': 'Post unliked successfully.'}, status=status.HTTP_200_OK)
