from django.contrib import admin
from .models import Menu


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')


admin.site.register(Menu, ServiceAdmin)