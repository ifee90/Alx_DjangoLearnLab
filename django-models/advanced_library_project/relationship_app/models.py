from django.db import models
from django.conf import settings

class Relationship(models.Model):
    user1 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='relationships_initiated'
    )
    user2 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='relationships_received'
    )
    status = models.CharField(max_length=50, default='pending')

    def __str__(self):
        return f"{self.user1.username} -> {self.user2.username} ({self.status})"
