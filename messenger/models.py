from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from hashid_field import HashidAutoField, HashidField


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)


class Profile(models.Model):
    user = models.OneToOneField('auth.User')


class Message(models.Model):
    sender = models.ForeignKey('auth.User', related_name='sender')
    recipient = models.ForeignKey('auth.User', related_name='recipient')
    body = models.TextField(max_length=100)

    def get_inbox(self):
        return Message.objects.filter(recipient=self.user)

    def get_outbox(self):
        return Message.objects.filter(sender=self.user)
