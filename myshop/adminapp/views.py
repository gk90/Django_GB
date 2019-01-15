from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse, reverse_lazy

from mainapp.models import Product, Category
from authapp.models import ShopUser
from .forms import CategoryForm ,ProductForm, UserForm

# Create your views here.

@user_passes_test(lambda u: u.is_superuser)
def myadmin_main_view(request):
	return render(request, 'adminapp/myadmin_main.html')

@user_passes_test(lambda u: u.is_superuser)
def users_view(request):
	users = ShopUser.objects.all()
	return render(request, 'adminapp/users.html', {'users': users})

@user_passes_test(lambda u: u.is_superuser)
def user_detail_view(request, pk):
	user = get_object_or_404(ShopUser, pk=pk)
	return render(request, 'adminapp/user_detail.html', {'user': user})

@user_passes_test(lambda u: u.is_superuser)
def user_create_view(request):
	if request.method == 'GET':
		form = UserForm()
		return render(request, 'adminapp/edit.html', {'form':form})
	else:
		form = UserForm(request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('myadmin:users'))
		else:
			return render(request, 'adminapp/edit.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def user_update_view(request, pk):
	user = get_object_or_404(ShopUser, pk=pk)
	if request.method == 'GET':
		form = UserForm(instance=user)
		return render(request, 'adminapp/edit.html', {'form':form})
	else:
		form = CategoryForm(request.POST, files=request.FILES, instance=user)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('myadmin:users'))
		else:
			return render(request, 'adminapp/edit.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def user_delete_view(request, pk):
	user = get_object_or_404(ShopUser, pk=pk)
	if request.method == 'POST':
		user.delete()
		return HttpResponseRedirect(reverse('myadmin:users'))
	else:
		return render(request, 'adminapp/user_delete_confirm.html', {'user': user})

class CategoryListView(ListView):
	model = Category
	template_name = 'adminapp/categories.html'
	paginate_by = 1

	@method_decorator(user_passes_test(lambda u: u.is_superuser))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

class CategoryDetailView(DetailView):
	model = Category
	template_name = 'adminapp/category_detail.html'

	@method_decorator(user_passes_test(lambda u: u.is_superuser))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

class CategoryCreateView(CreateView):
	model = Category
	template_name = 'adminapp/edit.html'
	success_url = reverse_lazy('myadmin:categories')
	form_class = CategoryForm

	@method_decorator(user_passes_test(lambda u: u.is_superuser))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

class CategoryUpdateView(UpdateView):
	model = Category
	template_name = 'adminapp/edit.html'
	success_url = reverse_lazy('myadmin:categories')
	form_class = CategoryForm

	@method_decorator(user_passes_test(lambda u: u.is_superuser))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

class CategoryDeleteView(DeleteView):
	model = Category
	template_name = 'adminapp/category_delete_confirm.html'
	success_url = reverse_lazy('myadmin:categories')

	@method_decorator(user_passes_test(lambda u: u.is_superuser))
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

@user_passes_test(lambda u: u.is_superuser)
def products_view (request):
	products = Product.objects.all()
	return render(request, 'adminapp/products.html', {'products': products})

@user_passes_test(lambda u: u.is_superuser)
def product_detail_view(request, pk):
	product = get_object_or_404(Product, pk=pk)
	return render(request, 'adminapp/product_detail.html', {'product': product})

@user_passes_test(lambda u: u.is_superuser)
def product_create_view(request):
	if request.method == 'GET':
		form = ProductForm()
		return render(request, 'adminapp/edit.html', {'form':form})
	else:
		form = ProductForm(request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('myadmin:products'))
		else:
			return render(request, 'adminapp/edit.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def product_update_view(request, pk):
	product = get_object_or_404(Product, pk=pk)
	if request.method == 'GET':
		form = ProductForm(instance=product)
		return render(request, 'adminapp/edit.html', {'form':form})
	else:
		form = ProductForm(request.POST, files=request.FILES, instance=product)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('myadmin:products'))
		else:
			return render(request, 'adminapp/edit.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def product_delete_view(request, pk):
	product = get_object_or_404(Product, pk=pk)
	if request.method == 'POST':
		product.delete()
		return HttpResponseRedirect(reverse('myadmin:products'))
	else:
		return render(request, 'adminapp/product_delete_confirm.html', {'product': product})