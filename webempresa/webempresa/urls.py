"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

"""Inicio home/
Historia about/
Servicios services/
Visítanos store/
Contacto contact/
Blog blog/
Sample sample/ (esta es para páginas de prueba)"""

urlpatterns = [
    # Incluimos una nota de url configuración.
    # Agregamos una url a las urlpatterns.
    path('', include('core.urls')),
    # Agregamos la urlpatterns de app service.
    path('service/', include("service.urls")),
    # Agregamos la urlpatterns de app blog.
    path('blog/', include("blog.urls")),
    # Agregamos la urlpatterns de app page.
    path('page/', include("pages.urls")),
    # Path Directorios de admin.
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
