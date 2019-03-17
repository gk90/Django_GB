
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'NAME': 'myshop',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'django',
        'PASSWORD': '123456',
        'HOST': 'localhost',
    }
}

