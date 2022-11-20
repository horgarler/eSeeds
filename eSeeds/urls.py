from django.contrib import admin
from django.urls import path
from eSeeds import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('catalogo/', views.catalogo, name='catalogo')
]