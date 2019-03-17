from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, DetailView, ListView
from .models import Product, Category
from django.conf import settings
from django.core.cache import cache
from django.db.models import Q


def get_categories():
    if settings.LOW_CACHE:
        key = 'categories'
        value = cache.get(key)
        if value is None:
            value = Category.objects.all()
            cache.set(key, value)
        return value
    else:
        return Category.objects.all()


def get_products():
    if settings.LOW_CACHE:
        key = 'products'
        value = cache.get(key)
        if value is None:
            value = Product.objects.all()
            cache.set(key, value)
        return value
    else:
        return Product.objects.all()


class Main(TemplateView):
    template_name = 'mainapp/index.html'
    title = 'Главная'
    objects = []
    categories = get_categories()
    products = get_products()

    for category in categories:
        object = {'category': category, 'products': []}
        objects.append(object)
        for product in products:
            if product.category.name == category.name:
                objects[objects.index(object)]["products"].append(product)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['objects'] = self.objects
        return context


class About(TemplateView):
    template_name = 'mainapp/about.html'
    title = 'About'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class Contacts(TemplateView):
    template_name = 'mainapp/contact.html'
    title = 'Contacts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class ProductDetail(DetailView):
    template_name = 'mainapp/product-details.html'
    model = Product


def product_by_category_view(request, pk, page):
    category = get_object_or_404(Category, pk=pk)
    """ используем обращение по fk для получения всех товаров указанной категории"""
    products = category.product_set.all()
    # products = Product.objects.filter(category=category)

    paginator = Paginator(products, 2)
    try:
        # получение объектов нужной сраницы
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        # последняя страница
        products_paginator = paginator.page(paginator.num_pages)

    content = {
        'title': 'Product_by_category',
        'products': products_paginator,
        'category': category,
    }
    return render(request, 'mainapp/product_by_category.html', content)
