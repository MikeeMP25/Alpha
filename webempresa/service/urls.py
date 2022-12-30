from django.urls import path
from . import views

urlpatterns = [
    # Paths del service
    path('', views.services, name="Menu"),
]
