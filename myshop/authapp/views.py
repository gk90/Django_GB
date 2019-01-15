from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from django.contrib import auth
from django.urls import reverse


def login(request):
	title = 'Авторизация'

	login_form = ShopUserLoginForm(data=request.POST or None)

	next = request.GET['next'] if 'next' in request.GET.keys() else ''

	if request.method == 'POST' and login_form.is_valid():
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)
		if user and user.is_active:
			auth.login(request, user)
			if 'next' in request.POST.keys():
				return HttpResponseRedirect(request.POST['next'])
			else:
				return HttpResponseRedirect(reverse('mainapp:index'))

	content = {
		'title': title,
		'login_form': login_form,
		'next': next
	}

	return render(request, 'authapp/login.html', content)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))

def register(request):
	title = 'Регистрация пользователя'

	if request.method == 'POST':
		register_form = ShopUserRegisterForm(request.POST, request.FILES)

		if register_form.is_valid():
			register_form.save()
			return HttpResponseRedirect(reverse('authapp:login'))
	else:
		register_form = ShopUserRegisterForm()

	content = {'title': title, 'register_form': register_form}

	return render(request, 'authapp/register.html', content)


def edit(request):
	title = 'Редактирование профиля'

	if request.method == 'POST':
		edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
		if edit_form.is_valid():
			edit_form.save()
			return HttpResponseRedirect(reverse('authapp:edit'))
	else:
		edit_form = ShopUserEditForm(instance=request.user)

	content = {'title': title, 'edit_form': edit_form}

	return render(request, 'authapp/edit.html', content)
