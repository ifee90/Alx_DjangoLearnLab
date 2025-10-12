from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Optional: a simple home route so the root URL doesn’t 404
def home(request):
    return JsonResponse({"message": "Welcome to the Social Media API"})

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ Accounts endpoints (register, login, follow/unfollow)
    path('api/accounts/', include('accounts.urls')),

    # ✅ Posts endpoints (create post, list posts, feed, comments, etc.)
    path('api/posts/', include('posts.urls')),

    # ✅ Optional root route for sanity check
    path('', home),
]
