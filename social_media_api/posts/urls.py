from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, user_feed, like_post, unlike_post

# Initialize router for standard CRUD operations
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    # Feed route — show posts from followed users
    path('feed/', user_feed, name='user_feed'),

    # Like/unlike routes for posts
    path('posts/<int:pk>/like/', like_post, name='like_post'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike_post'),

    # Include standard CRUD routes for posts and comments
    path('', include(router.urls)),
]
