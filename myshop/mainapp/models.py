from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    old_price = models.PositiveIntegerField()
    rating = models.PositiveIntegerField(verbose_name='Рейтинг', default=1)
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_new = models.BooleanField(default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def __str__(self):
        return "{}.{} ({}) количество на складе: {}".format(self.id, self.name, self.category, self.quantity)
