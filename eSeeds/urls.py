from django.contrib import admin
from django.urls import path
from eSeeds import views

urlpatterns = [

    #Estaticas
    path('', views.home, name= 'home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('politica_envio/', views.politica_envio, name='politica_envio'),
    path('politica_devolucion/', views.politica_devolucion, name='politica_devolucion'),
    path('datos_empresa/', views.datos_empresa, name='datos_empresa'),
    path('contacto/', views.contacto, name='contacto'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('entrega/', views.entrega, name="entrega"),

    #Requieren id
    path('catalogo/<int:producto_id>/', views.detalles_producto, name="producto"),

    #Carro y pago
    path('carro/', views.carro, name="carro"),
    path('agregar/<int:producto_id>/', views.agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_carro, name="CLS"),
    path('cargo/', views.cargo, name="cargo"),
    path('contrareembolso/', views.contrareembolso, name="contrareembolso"),
    path('pasarela/', views.pasarela, name="pasarela"),
    path('pago_exitoso/', views.pago_exitoso, name="pago_exitoso"),
]