from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from eSeeds.forms import ClienteForm, atencionClienteForm
from eSeeds.models import *
from eSeeds.carro import *
from eSeeds.context_processor import *
from django.core.mail import send_mail
from semillas.settings import EMAIL_HOST_USER
import stripe
stripe.api_key = 'sk_test_51MBWRLBRQnkF6gUbkUCcj4WkFdD7iMoity5cyO2xZEibjFKOgvZ8WR34KZQIYbgnz7CHw2lyFvSZTCjHDtOlCcGW00FWkkQ1MN'

def home(request):
    return render(request, 'home.html')

def catalogo(request):
    busqueda = request.GET.get("buscar")
    productos = Producto.objects.all()

    if busqueda:
        productos = Producto.objects.filter(
            Q(nombre__icontains = busqueda) | 
            Q(descripcion__icontains = busqueda)
        ).distinct()
    return render(request, 'catalogo.html', {'productos':productos})
    #esto devuelve todos los productos de la base de datos (para el catalogo)

def politica_envio(request):
    return render(request, 'politica_envio.html')

def politica_devolucion(request):
    return render(request, 'politica_devolucion.html') 

def datos_empresa(request):
    return render(request, 'datos_empresa.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

def entrega(request):
    return render(request, 'entrega.html')

########################### FICHA PRODUCTO

def detalles_producto(request, producto_id):
    if request.method == 'GET':
        producto = get_object_or_404(Producto, pk=producto_id)
        return render(request, 'producto.html', {'producto': producto}) #se le pasa lo que está entre ''
    else:   #(POST en la mayoria)
        try:
            producto = get_object_or_404(Producto, pk=producto_id)
            ##SETEAR ATRIBUTO ENN BBDD
            setattr(producto, 'disponibilidad', True)
            producto.save()
            ###############################

            #############AGREGAR PRODUCTO AL CARRITO###############
            #carro = Carro(request)
            #carro.agregar(servicio)
            ###############################

            #return redirect('carro')
        except ValueError:
            return render(request, 'producto.html', {'producto': producto})


################################ CARRO COMPRAS

def carro(request):
    return render(request, 'carro.html')

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto)
    return redirect("carro")    #€l name que se le dio en urls.py

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto)
    return redirect("carro")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar(producto)
    return redirect("carro")

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar()
    return redirect("carro")

def contrareembolso(request):
    return render(request, 'contrareembolso.html')

def cargo_contrareembolso(request):
    if request.method == 'POST':
        nombre = request.POST["nombre"]
        apellidos = request.POST["apellidos"]
        direccion = request.POST["direccion"]
        poblacion = request.POST["poblacion"]
        postal = request.POST["postal"]
        email = request.POST["email"]

        pedido_list = Pedido.objects.create(
            nombre = request.POST["nombre"],
            apellidos = request.POST["apellidos"],
            direccion = request.POST["direccion"],
            poblacion = request.POST["poblacion"],
            postal = request.POST["postal"],
            seguimiento = 0,
            email = request.POST["email"]
        )

        cantidad = total_carro(request)
        valor = int(cantidad.get('total_carro'))

        lista_carro = ""

        for key, value in request.session.items():
            if key == 'carro':
                for id in value:
                    producto_id = value[id]['producto_id']
                    lista_carro += "· " + str(value[id]['nombre']) + ' Cantidad: ' + str(value[id]['cantidad']) + "\n"
                    message = "Pedido realizado, datos de envío:\n" + str(nombre) + " " + str(apellidos) + "\n" + str(direccion) + " " + str(poblacion) + " (" + str(postal) + ")\nCon email de contacto: " + str(email) + "\n\nId del pedido: " + str(pedido_list.id) + '\n' + str(lista_carro) + "\nCoste total: " + str(valor) + "€\nPor Favor tenga preparado el dinero para cuando llegue su pedido para poder pagar al repartidor.\n\nGracias por confiar en nuestros servicios.\n\n"
    
        subject = "Pago exitoso"
        email_from = EMAIL_HOST_USER
        recipient_list = [request.POST['email']]

        send_mail(subject, message, email_from, recipient_list)

        carro = Carro(request)
        carro.limpiar()
    return redirect('pago_exitoso') 

def pasarela(request):
    return render(request, 'pasarela.html')

def cargo(request):
    if request.method == 'POST':

        nombre = request.POST["nombre"]
        apellidos = request.POST["apellidos"]
        direccion = request.POST["direccion"]
        poblacion = request.POST["poblacion"]
        postal = request.POST["postal"]
        email = request.POST["email"]

        
        customer = stripe.Customer.create(
            name = nombre + apellidos,
            email = email,
            source = request.POST["stripeToken"]
        )

        pedido_list = Pedido.objects.create(
            nombre = request.POST["nombre"],
            apellidos = request.POST["apellidos"],
            direccion = request.POST["direccion"],
            poblacion = request.POST["poblacion"],
            postal = request.POST["postal"],
            seguimiento = 0,
            email = request.POST["email"]
        )

        cantidad = total_carro(request)
        valor = int(cantidad.get('total_carro'))
        id_pedido = request.POST['stripeToken']

        charge = stripe.Charge.create(
            customer = customer,
            amount = valor*1000,
            currency = 'mxn',
            description = 'Pago exitoso'
        )

        lista_carro = ""

        for key, value in request.session.items():
            if key == 'carro':
                for id in value:
                    producto_id = value[id]['producto_id']
                    lista_carro += "· " + str(value[id]['nombre']) + ' Cantidad: ' + str(value[id]['cantidad']) + "\n"
                    message = "Pedido realizado, datos de envío:\n" + str(nombre) + " " + str(apellidos) + "\n" + str(direccion) + " " + str(poblacion) + " (" + str(postal) + ")\nCon email de contacto: " + str(email) + "\n\nId del pedido: " + str(pedido_list.id) + '\n' + str(lista_carro) + "\nCoste total: " + str(valor) + "€\n\nGracias por confiar en nuestros servicios.\n\n"
    
        subject = "Pago exitoso"
        email_from = EMAIL_HOST_USER
        recipient_list = [request.POST['email']]

        send_mail(subject, message, email_from, recipient_list)

        carro = Carro(request)
        carro.limpiar()
    return redirect('pago_exitoso') 
       

def pago_exitoso(request):
    return render(request, 'pago_exitoso.html')

##################### REGISTRO DE CLIENTE

def registroCliente(request):
    if request.method == 'GET':
        return render(request, 'cliente.html', {'form' : ClienteForm})
    else:
        try:
            form = ClienteForm(request.POST)
            nuevo_cliente = form.save(commit= False)
            nuevo_cliente.save()
            return redirect('home')
        except ValueError:
            return render(request, 'cliente.html', {'form' : ClienteForm, 'error' : form.errors})

####################### SEGUIMIENTO

def seguimiento(request):
    queryset=request.GET.get("buscar")
    servicios = []
    if queryset:
        servicios = Pedido.objects.filter(
            Q(id = queryset)
        )
    return render(request, 'seguimiento.html', {'seguimiento' : servicios})

####################### ATENCION AL CLIENTE

def atencion_cliente(request):
    if request.method == 'GET':

        return render(request, 'atencion_cliente.html', {'form' : atencionClienteForm})
    else:
        try:
            form = atencionClienteForm(request.POST)
            nuevo_cliente = form.save(commit= False)
            nuevo_cliente.save()
            return redirect('home')
        except ValueError:
            return render(request, 'atencion_cliente.html', {'form' : atencionClienteForm, 'error' : form.errors})


def mandar_correo(request):
    if request.method == 'POST':

        subject = ""

        if int(request.POST["tipo_consulta"]) == 0:
            subject += "Consulta de " + str(request.POST["nombre"])
        elif int(request.POST["tipo_consulta"]) == 1:
            subject += "Reclamo de " + str(request.POST["nombre"])
        elif int(request.POST["tipo_consulta"]) == 2:
            subject += "Sugerencia de " + str(request.POST["nombre"])
        elif int(request.POST["tipo_consulta"]) == 3:
            subject += "Felicitaciones de " + str(request.POST["nombre"])
        
        message = str(request.POST["correo"]) + " dice:\n" + str(request.POST["mensaje"])
        email_from = EMAIL_HOST_USER
        recipient_list = [EMAIL_HOST_USER]

        send_mail(subject, message, email_from, recipient_list)
    return redirect('correo_exitoso') 


def correo_exitoso(request):
    return render(request, 'correo_exitoso.html') 

