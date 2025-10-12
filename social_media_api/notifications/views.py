from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Notification
from .serializers import NotificationSerializer


# -----------------------------
# 1️⃣ List Notifications for Logged-in User
# -----------------------------
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Returns all notifications belonging to the logged-in user,
        with unread notifications appearing first.
        """
        user = self.request.user
        return Notification.objects.filter(recipient=user).order_by('is_read', '-timestamp')


# -----------------------------
# 2️⃣ Mark a Notification as Read
# -----------------------------
class MarkNotificationAsReadView(generics.GenericAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        """
        Marks a specific notification as read.
        """
        notification = get_object_or_404(Notification, pk=pk, recipient=request.user)
        notification.is_read = True
        notification.save()
        serializer = self.get_serializer(notification)
        return Response(serializer.data, status=status.HTTP_200_OK)
