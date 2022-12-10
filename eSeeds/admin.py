from django.contrib import admin
from eSeeds.models import Producto, Cliente, atencionCliente

# Register your models here.

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(atencionCliente)

