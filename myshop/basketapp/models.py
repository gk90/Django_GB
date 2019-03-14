from django.db import models
from django.conf import settings
from mainapp.models import Product
from django.utils.functional import cached_property


class BasketQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for object in self:
            object.product.quantity += object.quantity
            object.product.save()
        super().delete(*args, **kwargs)


class Basket(models.Model):
    objects = BasketQuerySet.as_manager()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="baskets")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время добавления', auto_now_add=True)

    def _get_product_cost(self):
        return self.product.price * self.quantity

    product_cost = property(_get_product_cost)

    cached_basket = []

    ##########################
    @cached_property
    def get_cached_objects(self):
        return Basket.objects.filter(user=self.user).select_related()

    ##########################
    def get_summary(self):
        items = self.get_cached_objects
        return {
            'total_quantity': sum(list(map(lambda x: x.quantity, items))),
            'total_cost': sum(list(map(lambda x: x.quantity * x.product.price, items))),
        }

    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user).select_related()

    @staticmethod
    def get_product(user, product):
        return Basket.objects.filter(user=user, product=product).select_related()

    @classmethod
    def get_products_quantity(cls, user):
        basket_items = cls.get_items(user)
        basket_items_dic = {}
        [basket_items_dic.update({item.product: item.quantity}) for item in basket_items]
        return basket_items_dic

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk)

    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)

    def delete(self):
        self.product.quantity += self.quantity
        self.product.save()
        super().delete()
