from django.urls import path
from . import views

urlpatterns = [
    # Paths del core
    path('', views.blog, name="Promotions"),
    path('category/<int:category_id>/', views.category, name="category"),
]
