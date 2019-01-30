from django.urls import path

from .views import *

app_name = 'basketapp'

urlpatterns = [
	path('', basket, name='basket'),
	path('add/<int:pk>/', basket_add, name='add'),
	path('remove/<int:pk>/', basket_remove, name='remove')
]