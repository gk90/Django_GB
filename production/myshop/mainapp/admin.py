from django.contrib import admin
from .models import Product, Category
from basketapp.models import Basket
from authapp.models import ShopUser, ShopUserProfile
from ordersapp.models import Order, OrderItem

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Basket)
admin.site.register(ShopUser)
admin.site.register(ShopUserProfile)
admin.site.register(Order)
admin.site.register(OrderItem)

