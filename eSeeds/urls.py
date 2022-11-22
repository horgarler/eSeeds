from django.contrib import admin
from django.urls import path
from eSeeds import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('politica_envio/', views.politica_envio, name='politica_envio'),
    path('datos_empresa/', views.datos_empresa, name='datos_empresa'),
    path('contacto/', views.contacto, name='contacto'),
]