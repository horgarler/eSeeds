from django.db import models

# Create your models here.

class Producto(models.Model):
    
    # nombre (str), precio (float), descripción (text), disponibilidad (bool)
    nombre = models.CharField(max_length= 100, blank=False, null=False)
    precio = models.FloatField(null=False)
    descripcion = models.TextField(max_length=255, blank=False, null=False)
    disponibilidad = models.BooleanField(blank=False, null=False)
    imagen = models.ImageField(null=True, upload_to='eSeeds/static/media')
