from django.shortcuts import render, HttpResponse

# Create your views here.
"""
Inicio home/

Historia about/

Servicios services/

Visítanos store/

Contacto contact/

Blog blog/

Sample sample/ (esta es para páginas de prueba)
"""


def home(request):
    return HttpResponse("<h1>Inicio</h1>")


def about(request):
    return HttpResponse("<h1>historia</h1>")


def services(request):
    return HttpResponse("<h1>Servicios</h1>")


def store(request):
    return HttpResponse("<h1>Visitanos</h1>")


def contact(request):
    return HttpResponse("<h1>Contactos</h1>")


def blog(request):
    return HttpResponse("<h1>Blog</h1>")


def sample(request):
    return HttpResponse("<h1>Sample</h1>")
