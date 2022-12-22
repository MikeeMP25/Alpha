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
from django.urls import path
from core import views

"""
Inicio home/

Historia about/

Servicios services/

Visítanos store/

Contacto contact/

Blog blog/

Sample sample/ (esta es para páginas de prueba)
"""

urlpatterns = [
    # Paths del core
    path('', views.home, name="Inicio"),
    path('about/', views.about, name="Historia"),
    path('services/', views.services, name="Servicio"),
    path('store/', views.store, name="Visitanos"),
    path('contact/', views.contact, name="Contacto"),
    path('blog/', views.blog, name="Blog"),
    path('sample/', views.sample, name="Sample"),
    # directoris de admin
    path('admin/', admin.site.urls),
]
