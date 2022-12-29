from django.shortcuts import render, get_object_or_404
from .models import Page


# Personalizamos la configuracion vistas
# y controlamos un error 404 para que sea mas especifico cuando salga un error 404
# mandamos por url un identificador id a sample.html quien recibira e enviara la variable
# Create your views here.
def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/sample.html', {'pages': page})
