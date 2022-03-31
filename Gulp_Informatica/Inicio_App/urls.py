from django import views
from django.urls import path
from .views import *



urlpatterns = [
    path('inicio/', InicioPage, name="inicio"),
    path('trabajos/', TrabajosPage,name="trabajos"),
    path('ventas/', VentasPage,name="ventas"),
    path('pedidos/', PedidosPage,name="pedidos"),
    path('trabajosform/', TrabajosFormulario,name="trabajosform"),
    path('ventasform/', VentasFormulario, name="ventasform"),
    path('pedidosform/', PedidosFormulario, name="pedidosform"),        
    path('buscarcliente/', BuscarCliente, name="buscarcliente"),
    
]
