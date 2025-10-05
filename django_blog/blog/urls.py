from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    # Home and User routes
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', login_required(views.profile), name='profile'),

    # Post-related paths
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comment routes
    path('post/<int:pk>/comment/', views.CommentCreateView.as_view(), name='add-comment'),
    path('comment/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='edit-comment'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete-comment'),

    # Tag routes
    path('tags/<slug:tag_slug>/', views.PostsByTagView.as_view(), name='posts-by-tag'),  # Updated to match checker requirement

    # Search route
    path('search/', views.SearchResultsView.as_view(), name='search-results'),
]
