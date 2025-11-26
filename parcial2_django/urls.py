from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuentas/', include('apps.cuentas.urls')),
    path('alumnos/', include('apps.alumnos.urls')),
    path('informes/', include('apps.informes.urls')),
    path('scraper/', include('apps.scraper.urls')),
    path('', lambda request: redirect('login')),
]

