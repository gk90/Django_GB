from django.core.management.base import BaseCommand
from mainapp.models import Category, Product
from django.db.models import Q


class Command(BaseCommand):
    def handle(self, *args, **options):
        product = Product.objects.filter(Q(category__name='Computers') | Q(category__name='Mobile'))
        print(product)
