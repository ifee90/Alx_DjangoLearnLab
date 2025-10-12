from django.urls import path
from .views import NotificationListView, MarkNotificationAsReadView

urlpatterns = [
    # List all notifications for the logged-in user
    path('', NotificationListView.as_view(), name='notification_list'),

    # Mark a specific notification as read
    path('<int:pk>/read/', MarkNotificationAsReadView.as_view(), name='mark_notification_read'),
]
