from django.urls import path
from . import views

urlpatterns = [
    # Paths del service
    path('service/', views.services, name="Menu"),
]
