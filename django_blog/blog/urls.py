from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),

    # Blog post CRUD URLs (updated to match ALX checker)
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),           # Create new post
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),      # Post detail
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'), # Update post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'), # Delete post
    path('posts/', views.PostListView.as_view(), name='posts'),                       # List all posts
]
