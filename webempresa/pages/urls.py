from django.urls import path
from . import views

# este es el metodo post url
urlpatterns = [
    # Paths de page
    path('<int:page_id>/<slug:page_slug>/', views.page, name="page"),
]
