from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from eSeeds.models import *
from eSeeds.carro import *
from eSeeds.context_processor import *
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

def contacto(request):
    return render(request, 'contacto.html')

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

def pasarela(request):
    return render(request, 'pasarela.html')

def cargo(request):
    if request.POST:
        cantidad = total_carro(request)
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

        charge = stripe.Charge.create(
            customer = customer,
            amount = cantidad,
            currency = 'eur',
            description = 'Pago articulos eSeeds'
        )
    redirect('pago_exitoso')    

def pago_exitoso(request):
    return render(request, 'pago_exitoso.html')