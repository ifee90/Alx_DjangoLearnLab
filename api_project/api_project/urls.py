from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # import token view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # connects to your api app
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # token retrieval endpoint
]
