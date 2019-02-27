from django.urls import path
from .views import *


app_name = 'adminapp'

urlpatterns = [
    path('', myadmin_main_view, name='main'),

    path('users', users_view, name='users'),
    path('users/detail/<int:pk>', user_detail_view, name='user'),
    path('users/create/', user_create_view, name='create_user'),
    path('users/update/<int:pk>', user_update_view, name='user_update'),
    path('users/delete/<int:pk>', user_delete_view , name='user_delete'),

    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/detail/<int:pk>', CategoryDetailView.as_view(), name='category'),
    path('categories/create/', CategoryCreateView.as_view(), name='create_category'),
    path('categories/update/<int:pk>', CategoryUpdateView.as_view(), name='update_category'),
    path('categories/delete/<int:pk>', CategoryDeleteView.as_view(), name='delete_category'),

    path('products/', products_view, name='products'),
    path('products/detail/<int:pk>', product_detail_view, name='product'),
    path('products/create/product', product_create_view, name='create_product'),
    path('products/update/<int:pk>', product_update_view, name='update_product'),
    path('products/delete/<int:pk>', product_delete_view, name='delete_product')
]