from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Message, Notification

@receiver(post_save, sender=Message)
def create_msg_notofication(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            title=f'You have a new message from {instance.name}',
            message=instance)
