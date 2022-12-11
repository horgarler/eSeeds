from django.db import models

# Create your models here.

class Producto(models.Model):
    
    # nombre (str), precio (float), descripción (text), disponibilidad (bool)
    nombre = models.CharField(max_length= 100, blank=False, null=False)
    precio = models.FloatField(null=False)
    descripcion = models.TextField(max_length=255, blank=False, null=False)
    disponibilidad = models.BooleanField(blank=False, null=False)
    imagen = models.ImageField(null=True, upload_to='media')

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'

#Seguimiento
opciones_seguimiento = [
    [0, "Procesando"],
    [1, "En envío"],
    [2, "Entregado"]
]

class Pedido(models.Model):
    id_pedido = models.TextField(null=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    poblacion = models.CharField(max_length=50)
    postal = models.IntegerField()
    email = models.EmailField()
    seguimiento = models.IntegerField(choices=opciones_seguimiento , null = True)
    
    def str(self):
        return self.nombre
        
class Cliente(models.Model):

    nombre = models.CharField(max_length= 100, blank=False, null=False)
    apellidos = models.CharField(max_length= 100, blank=False, null=False)
    nacimiento = models.DateField(null=False, blank=False, help_text= 'Formato de fecha: AAAA-MM-DD')
    email = models.EmailField(unique=True, null=False,blank=False)

#Atención al cliente
opciones_conultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]

class atencionCliente(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_conultas)
    mensaje = models.TextField()

    def str(self):
        return self.nombre