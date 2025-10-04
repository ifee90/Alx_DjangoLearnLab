from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page ✅
    path('register/', views.register, name='register'),  # Registration page ✅
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),  # Login page ✅
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),  # Logout page ✅
    path('profile/', views.profile, name='profile'),  # Profile page ✅
    path('posts/', views.posts, name='posts'),  # Blog posts page ✅
]
