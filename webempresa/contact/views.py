from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactFrom


# Create your views here.
# En este metodo utilizamos el method=GET para obtener la pagina y POST para enviar datos atravez del formulario creado
def contact(request):
    # aqui instanciamos lo que ya tenemos creado de la clase ContactFrom
    contact_form = ContactFrom()
    # Como estamos trabajando sobre el mismo templa solo cambia su method de respuesta get o post validamos cual recibe
    # de la plantilla
    if request.method == "POST":
        # cargamos la plantilla form con los datos enviar en el POST
        contact_form = ContactFrom(data=request.POST)
        # aqui hicimos una pequeña validacion que no acepte campos vacios
        if contact_form.is_valid():
            # aqui guardamos en variables locales obtemos los datos de entrada (Post)
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # aqui redireccionamos la pagina y utilizamos reverse que se encarga de redireccionar la urls
            # de forma dinamíca django

            # ENVIAMOS EL CORREO Y REDIRECCIONAMOS
            # cargamos el contenido de un mensaje de correo en un objeto que tiene la estructura de un correo
            # nombre quien envio el correo y el destinatario y el contenido o mensaje
            email = EmailMessage(
                "MAICK POOL-BAR: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contesar@inbox.mailtrap.io",
                ["miguel.miranda@madd.com.mx"],
                reply_to=[email]
            )
            # controlamos los posibles errores al enviar un correo
            try:
                email.send()
                return redirect(reverse('Contacto') + "?ok")
            except:
                return redirect(reverse('Contacto') + "?fail")

    # aqui renderizamos al un pagina html estructura con FORM
    # objeto render(objeto request de respuesta/ la direccion de html donde ira a buscar/
    # mandamos un diccionario con el from ya cargado, estructurado y ordenado.
    return render(request, 'contact/contact.html', {'form': contact_form})
