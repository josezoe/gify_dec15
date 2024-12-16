# multivendor_app/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('vendors/', include('vendors.urls', namespace='vendors')),
    path('products/', include('products.urls', namespace='products')),
    path('reports/', include('reports.urls', namespace='reports')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', lambda request: redirect('users:login'), name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)