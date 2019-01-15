from django.contrib import admin
from .models import Product, Category
from basketapp.models import Basket
from authapp.models import ShopUser

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Basket)
admin.site.register(ShopUser)