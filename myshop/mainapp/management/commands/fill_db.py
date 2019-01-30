from django.core.management.base import BaseCommand
from mainapp.models import Category, Product
from authapp.models import ShopUser

import json, os


JSON_PATH = 'mainapp/json'

def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)



class Command(BaseCommand):
    help = 'Fill DB new data'
    print('Запуск скрипта')

    def handle(self, *args, **options):
        categories = loadFromJSON('categories')

        Category.objects.all().delete()

        for category in categories:
            new_category = Category(**category)
            new_category.save()

        products = loadFromJSON('products')

        for product in products:
            category_name = product["category"]
            _category = Category.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        super_user = ShopUser.objects.create_superuser('admin', 'admin@myshop.local', '123456', age=28)

