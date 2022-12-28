#importamos los modelos de django de base de datos para poder crear tablas con sus campos
# correspodinetes
from django.db import models
#importamos de django la utilizades donde mandamos a llamar la fecha
from django.utils.timezone import now
#Importamos de la paqueteria de djando los campos que crea defecto de Usuarios
from django.contrib.auth.models import User


# Create your models here.
# this is of category
class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Ultima actualización")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["-created"]

    def __str__(self):
        return self.name


# this is of post(entrada)
class Post(models.Model):
    # campos normales de la tabla
    title = models.CharField(max_length=100, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicacion", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    # campos que tiene referencias de la tabla category y llave foranea de la tabla User
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Ultima actualización")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created"]

    def __str__(self):
        return self.title


