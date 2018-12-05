from django.shortcuts import render
from .models import Product, Category, Subcategory

# Create your views here.
def main_view (request):
    same_category = Category.objects.all()
    same_subcategory = Subcategory.objects.all()
    same_products = Product.objects.all()

    content = {
        'title': 'main',
        'same_products': same_products,
        'same_category': same_category,
        'same_subcategory': same_subcategory,
    }

    return render(request, 'mainapp/index.html', content)

def about_view (request):
    return render(request, 'mainapp/about.html', {'title': 'about'})

def account_view (request):
    return render(request, 'mainapp/account.html', {'title': 'account'})

def cart_view (request):
    return render(request, 'mainapp/cart.html', {'title': 'cart'})

def checkout_view (request):
    return render(request, 'mainapp/checkout.html', {'title': 'checkout'})

def contact_view (request):
    return render(request, 'mainapp/contact.html', {'title': 'contact'})

def account_view (request):
    return render(request, 'mainapp/my-account.html', {'title': 'my-account'})

def details_view (request):
    return render(request, 'mainapp/product-details.html', {'title': 'details'})

def shop_view (request):
    return render(request, 'mainapp/shop.html', {'title': 'shop'})

def shop_list_view (request):
    return render(request, 'mainapp/shop-list.html', {'title': 'shoplist'})

def wishlist_view (request):
    return render(request, 'mainapp/wishlist.html', {'title': 'wishlist'})

