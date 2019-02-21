from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from .models import Basket
from mainapp.models import Product, Category

@login_required
def basket(request):
	basket_items = Basket.objects.filter(user=request.user).order_by('product__category')
	content = {
		'title': 'basket',
		'basket_items': basket_items,
	}
	return render(request, 'basketapp/basket.html', content)

@login_required
def basket_add(request, pk):
	if 'login' in request.META.get('HTTP_REFERER'):
		return HttpResponseRedirect(reverse('mainapp:product', args=[pk]))

	product = get_object_or_404(Product, pk=pk)
	old_basket_item = Basket.objects.filter(user=request.user, product=product)

	if old_basket_item:
		old_basket_item[0].quantity += 1
		old_basket_item[0].save()
	else:
		new_basket_item = Basket(user=request.user, product=product)
		new_basket_item.quantity += 1
		new_basket_item.save()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_remove(request, pk):
	basket_record = get_object_or_404(Basket, pk=pk)
	basket_record.delete()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
