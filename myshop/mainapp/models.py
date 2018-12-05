from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=32, unique=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    display = models.CharField(max_length=32, unique=True)

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
    sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    new = models.BooleanField(default=0)
    discount = models.IntegerField(default=0)


    def __str__(self):
        return self.name