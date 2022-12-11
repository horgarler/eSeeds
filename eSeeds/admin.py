from django.contrib import admin
from eSeeds.models import Producto, Cliente, atencionCliente, Pedido

# Register your models here.

admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Cliente)
admin.site.register(atencionCliente)

