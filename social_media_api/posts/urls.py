from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, user_feed, like_post, unlike_post

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('feed/', user_feed, name='user_feed'),  # ✅ Feed route
    path('posts/<int:pk>/like/', like_post, name='like_post'),  # ✅ Like a post
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike_post'),  # ✅ Unlike a post
    path('', include(router.urls)),
]
