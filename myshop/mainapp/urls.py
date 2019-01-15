from django.contrib import admin
from django.urls import path
from mainapp import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('product/<int:pk>/', views.product, name='product'),
    path('product_by_category/<int:pk>/<int:page>/', views.product_by_category_view, name='product_by_category')
]
