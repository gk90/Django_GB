from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.timezone import now
from datetime import timedelta
import random
import hashlib

from django.db.models.signals import post_save
from django.dispatch import receiver


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)
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


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж'),
    )

    user = models.OneToOneField(ShopUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='теги', max_length=128, blank=True)
    aboutMe = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    language = models.CharField(verbose_name='язык', max_length=30, blank=True)
    url = models.URLField(verbose_name='url', blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=ShopUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()
