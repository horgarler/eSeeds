from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from eSeeds.forms import ClienteForm, atencionClienteForm
from eSeeds.models import *
from eSeeds.carro import *

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