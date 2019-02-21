from django.contrib import admin
from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainapp'

urlpatterns = [
    path('', main_view, name='index'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('product/<int:pk>/', product, name='product'),
    path('product_by_category/<int:pk>/<int:page>/', product_by_category_view, name='product_by_category')
]
