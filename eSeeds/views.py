from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from eSeeds.models import *


# Create your views here.

def home(request):
    return render(request, 'home.html')

def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo.html', {'productos':productos})
    #esto devuelve todos los productos de la base de datos (para el catalogo)

def politica_envio(request):
    return render(request, 'politica_envio.html')

def datos_empresa(request):
    return render(request, 'datos_empresa.html')

def contacto(request):
    return render(request, 'contacto.html')

def entrega(request):
    return render(request, 'entrega.html')

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
            #carrito = Carrito(request)
            #carrito.agregar(servicio)
            ###############################

            #return redirect('carrito')
        except ValueError:
            return render(request, 'producto.html', {'producto': producto})