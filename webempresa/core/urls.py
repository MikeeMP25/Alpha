from django.urls import path
from . import views

urlpatterns = [
    # Paths del core
    path('', views.home, name="Inicio"),
    path('about/', views.about, name="Historia"),
    path('store/', views.store, name="Visitanos"),
    path('contact/', views.contact, name="Contacto"),
]