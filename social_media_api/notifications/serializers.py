from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    recipient = serializers.StringRelatedField(read_only=True)
    actor = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Notification
        fields = [
            'id',
            'recipient',
            'actor',
            'verb',
            'timestamp',
            'is_read'
        ]
        read_only_fields = ['recipient', 'actor', 'timestamp']
