from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.timezone import now
from datetime import timedelta
import random
import hashlib

class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(
        now() + timedelta(hours=48)), null=True
    )

    def activation_key_expires_update(self):
        new_activation_key_expires = now() + timedelta(hours=48)
        return new_activation_key_expires

    def activation_key_generator(self):
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        activation_key = hashlib.sha1((self.email + salt).encode('utf8')).hexdigest()
        return activation_key

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True
