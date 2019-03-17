from django.contrib import admin
from django.urls import include, path, re_path 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('mainapp.urls', namespace='mainapp')),
    path('auth/', include('authapp.urls', namespace='authapp')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('myadmin/', include('adminapp.urls', namespace='myadmin')),
    path('auth/verify/google/oauth2/', include("social_django.urls", namespace="social")),
    path('admin/', admin.site.urls),
    path('order/', include('ordersapp.urls', namespace='order')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [re_path(r'^__debug__/', include(debug_toolbar.urls))] 
