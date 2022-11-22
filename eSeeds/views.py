from django.shortcuts import render
from eSeeds.models import *

# Create your views here.

def home(request):
    return render(request, 'home.html')

def catalogo(request):
    semillas = Semilla.objects.all()
    return render(request, 'catalogo.html', {'semillas':semillas})
    #esto devuelve todas las semillas de la base de datos (para el catalogo)

def politica_envio(request):
    return render(request, 'politica_envio.html')

def datos_empresa(request):
    return render(request, 'datos_empresa.html')

def contacto(request):
    return render(request, 'contacto.html')