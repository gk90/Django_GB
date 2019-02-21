from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category


# Create your views here.
def main_view(request):

    categories = Category.objects.all()
    products = Product.objects.all()

    content = {
        'title': 'main',
        'products': products,
        'categories': categories,
    }

    return render(request, 'mainapp/index.html', content)

def about_view(request):
    content = {
        'title': 'about',
    }
    return render(request, 'mainapp/about.html', content)

def contact_view(request):
    content = {
        'title': 'contact',
    }
    return render(request, 'mainapp/contact.html', content)

def product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    content = {
        'title': 'product',
        'product': product,
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
    }
    return render(request, 'mainapp/product_by_category.html', content)