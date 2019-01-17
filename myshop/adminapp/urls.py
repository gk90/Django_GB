from django.urls import path
from adminapp import views

app_name = 'adminapp'

urlpatterns = [
    path('', views.myadmin_main_view, name='main'),

    path('users', views.users_view, name='users'),
    path('users/detail/<int:pk>', views.user_detail_view, name='user'),
    path('users/create/', views.user_create_view, name='create_user'),
    path('users/update/<int:pk>', views.user_update_view, name='user_update'),
    path('users/delete/<int:pk>', views.user_delete_view , name='user_delete'),

    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categories/detail/<int:pk>', views.CategoryDetailView.as_view(), name='category'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='create_category'),
    path('categories/update/<int:pk>', views.CategoryUpdateView.as_view(), name='update_category'),
    path('categories/delete/<int:pk>', views.CategoryDeleteView.as_view(), name='delete_category'),

    path('products/', views.products_view, name='products'),
    path('products/detail/<int:pk>', views.product_detail_view, name='product'),
    path('products/create/product', views.product_create_view, name='create_product'),
    path('products/update/<int:pk>', views.product_update_view, name='update_product'),
    path('products/delete/<int:pk>', views.product_delete_view, name='delete_product')
]