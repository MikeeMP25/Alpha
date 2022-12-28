from django.shortcuts import render
from .models import Menu

# Create your views here.

def services(request):
    menus = Menu.objects.all()

    return render(request, 'service/services.html', {'menu': menus})
