from .models import Link


# hemos creado un proceso donde podemos mandar datos a cualquier templeate creado
def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    print(ctx)
    return ctx
