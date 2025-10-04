from django.contrib import admin
from django.urls import path, include  # make sure to import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # include the blog app URLs
]

