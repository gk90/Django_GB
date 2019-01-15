from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Product, Category
from basketapp.models import Basket

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def getBasket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []

def main_view(request):

    categories = Category.objects.all()
    products = Product.objects.all()

    content = {
        'title': 'main',
        'products': products,
        'categories': categories,
        'basket': getBasket(request.user)
    }

    return render(request, 'mainapp/index.html', content)

def about_view(request):
    content = {
        'title': 'about',
        'basket': getBasket(request.user)
    }
    return render(request, 'mainapp/about.html', content)

def contact_view(request):
    content = {
        'title': 'contact',
        'basket': getBasket(request.user)
    }
    return render(request, 'mainapp/contact.html', content)

def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = getBasket(request.user)

    content = {
        'title': 'product',
        'product': product,
        'basket': basket
    }
    return render(request, 'mainapp/product-details.html', content)

def product_by_category_view(request, pk, page):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)

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
        'basket': getBasket(request.user)
    }
    return render(request, 'mainapp/product_by_category.html', content)