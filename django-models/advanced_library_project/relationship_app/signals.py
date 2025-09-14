from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.apps import apps

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a UserProfile for new users **only if** a UserProfile model exists
    in relationship_app. This avoids import errors when UserProfile was moved
    or removed.
    """
    if not created:
        return

    try:
        # Try to get the UserProfile model dynamically.
        UserProfile = apps.get_model('relationship_app', 'UserProfile')
    except LookupError:
        # Model doesn't exist in relationship_app — nothing to do.
        return

    if UserProfile is None:
        return

    # Create profile only if one doesn't already exist
    if not UserProfile.objects.filter(user=instance).exists():
        # Default role set to 'Member' (adjust if you want another default)
        UserProfile.objects.create(user=instance, role='Member')
