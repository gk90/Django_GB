from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib import auth
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from .models import ShopUser
from .forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm, ShopUserProfileEditForm
from django.db import transaction


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


def register(request, success_registration=0):
    title = 'Регистрация пользователя'
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                return HttpResponseRedirect(reverse('authapp:register', args=['success']))
            else:
                return HttpResponseRedirect(reverse('authapp:register'))
    else:
        register_form = ShopUserRegisterForm()

    content = {'title': title, 'register_form': register_form}
    if success_registration:
        content['register'] = 'success'

    return render(request, 'authapp/register.html', content)

@transaction.atomic
def edit(request):
    title = 'Редактирование профиля'
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        profile_form = ShopUserProfileEditForm(request.POST, instance=request.user.shopuserprofile)
        if edit_form.is_valid() and profile_form.is_valid():
            # При сохраненнии пользователя сохраняется профиль через receiver
            edit_form.save()
            return HttpResponseRedirect(reverse('authapp:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)
        profile_form = ShopUserProfileEditForm(instance=request.user.shopuserprofile)

    content = {'title': title, 'edit_form': edit_form, 'profile_form': profile_form}
    return render(request, 'authapp/edit.html', content)


def send_verify_mail(user):
    verify_link = reverse('authapp:verify', args=[
                          user.email, user.activation_key])
    subject = 'Подтверждение учетной записи {}'.format(user.username)
    message = 'Для подтверждения учетной записи {} на портале {} перейдите по ссылке:\n{}{}'.format(
        user.username,
        settings.DOMAIN_NAME,
        settings.DOMAIN_NAME,
        verify_link
    )
    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify_user(request, email, activation_key, backend='django.contrib.auth.backends.ModelBackend'):
    user = get_object_or_404(ShopUser, activation_key=activation_key)

    if user.is_activation_key_expired():
        user.activation_key = user.activation_key_generator()
        user.activation_key_expires = user.activation_key_expires_update()
        user.save()
        send_verify_mail(user)
        return render(request, 'authapp/activation.html')
    else:
        user.is_active = True
        user.activation_key_expires = None
        user.save()
        auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return render(request, 'authapp/activation.html')
