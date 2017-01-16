import hashlib
from urllib.parse import urlencode

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def gravatar_url(self):
        url = 'https://www.gravatar.com/avatar/%s?%s' % (
            hashlib.md5(self.user.email.lower().encode('utf-8')).hexdigest(),
            urlencode(dict(s=30)),
        )
        return url


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
