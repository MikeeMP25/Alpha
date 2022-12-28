# importamos la vista o cofiguracion predetermida de superuser(admin) Administrador
from django.contrib import admin
# importamos los modelos de categorias y de entradas
from .models import Category, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('update', 'created')


class PostAdmin(admin.ModelAdmin):
    # Se visualiza en los campos de edicion y registro de la vista del administrador
    readonly_fields = ('created', 'update')
    # Se visualiza en la pestaña post admin/blog/post en la tabla de para modificar algun registro
    list_display = ('title', 'author', 'published', 'post_categories')
    # Personalizando las funciones del jsgrind
    ordering = ('author', 'published')
    # Este es un buscador por campos tu espeficicar en que campos va a buscar dicha informacion
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    # Utilizamos un filtro por fechas (buscador o rodenador por fechas)
    date_hierarchy = 'published'

    # Personalizamos la ventana del administrador agregamos una lista de filtros que juega con el jsgrid
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        return ','.join([c.name for c in obj.categories.all().order_by('name')])

    post_categories.short_description = 'Categorias'



admin.site.register(Category, CategoryAdmin)

admin.site.register(Post, PostAdmin)
