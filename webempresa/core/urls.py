from django.urls import path
from . import views

urlpatterns = [
    # Paths del core
    path('', views.home, name="Inicio"),
    path('about/', views.about, name="Historia"),
    path('services/', views.services, name="Servicio"),
    path('store/', views.store, name="Visitanos"),
    path('contact/', views.contact, name="Contacto"),
    path('blog/', views.blog, name="Blog"),
    path('sample/', views.sample, name="Sample"),
]