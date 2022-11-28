from django.shortcuts import render
from eSeeds.models import *

# Create your views here.

def home(request):
    return render(request, 'home.html')

def catalogo(request):
    semillas = Semilla.objects.all()
    return render(request, 'catalogo.html', {'semillas':semillas})
    #esto devuelve todas las semillas de la base de datos (para el catalogo)
