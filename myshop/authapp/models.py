from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.PositiveIntegerField(verbose_name= 'возраст')
