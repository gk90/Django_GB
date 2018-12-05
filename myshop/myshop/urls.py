"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view, name = 'index'),
    path('about/', views.about_view, name = 'about'),
    path('account/', views.account_view, name = 'account'),
    path('cart/', views.cart_view, name = 'cart'),
    path('checkout/',views.checkout_view, name = 'checkout'),
    path('contact/', views.contact_view, name = 'contact'),
    path('my-account/', views.account_view, name = 'my-account'),
    path('product-details/', views.details_view, name = 'product-details'),
    path('shop/', views.shop_view, name = 'shop'),
    path('shop-list/', views.shop_list_view, name = 'shop-list'),
    path('wishlist/', views.wishlist_view, name = 'wishlist'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
