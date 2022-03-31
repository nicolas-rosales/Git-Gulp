from ast import Return
from django.http import HttpResponse
from django.shortcuts import render
from Inicio_App.models import Trabajos, Ventas, Pedidos
from Inicio_App.forms import TrabajosForm, VentasForm, PedidosForm
from .views import *


def InicioPage(request):
    return render(request,"InicioPage.html")

def VentasPage(request):
    return render(request, "VentasPage.html")

def PedidosPage(request):
    return render(request, "PedidosPage.html")

def TrabajosPage(request):
    return render(request, "TrabajosPage.html")

 # ----- def de formularios ----- #

################ -------- Trabajos ----------- ############### 

def TrabajosFormulario(request):
    if request.method == 'POST':
        trabajosform = TrabajosForm(request.POST)
        print(trabajosform)

        if trabajosform.is_valid:
            data = trabajosform.cleaned_data
            trabajosform_nuevo = Trabajos(nombre_producto=data['nombre_producto'],
                                          precio_instalacion=data['precio_instalacion'],
                                          cliente=data['cliente'])
            trabajosform_nuevo.save()
        return render(request, "TrabajosPage.html")
    else:
        trabajosform_form = TrabajosForm()

        return render(request, "TrabajosForm.html", {"formulario":trabajosform_form})

################ -------- Ventas ----------- ###############

def VentasFormulario(request):
    if request.method == 'POST':
        ventasform = VentasForm(request.POST)
        print(ventasform)

        if ventasform.is_valid:
            data = ventasform.cleaned_data
            ventasform_nuevo = Ventas(producto=data['producto'],
                                          valor_producto=data['valor_producto'],
                                          precio_producto=data['precio_producto'])
            ventasform_nuevo.save()
        return render(request, "VentasPage.html")
    else:
        ventasform_form = VentasForm()

        return render(request, "VentasForm.html", {"formulario":ventasform_form})

################ -------- Pedidos ----------- ###############

def PedidosFormulario(request):
    if request.method == 'POST':
        pedidosform = PedidosForm(request.POST)
        print(pedidosform)

        if pedidosform.is_valid:
            data = pedidosform.cleaned_data
            pedidosform_nuevo = Pedidos(producto=data['producto'],
                                          precio=data['precio'],
                                          cliente=data['cliente'])
            pedidosform_nuevo.save()
        return render(request, "PedidosPage.html")
    else:
        pedidosform_form = PedidosForm()

        return render(request, "PedidosForm.html", {"formulario":pedidosform_form})
    

############# ------ Busqueda de Cliente ------ ###############

def BuscarCliente(request):
    data = request.GET.get('cliente', "")
    print(data)
    if data:
        cliente_ = Trabajos.objects.filter(cliente__icontains = data)
        return render(request,"BusquedaCliente.html", {"cliente":cliente_, "id":data})
    return render(request,"BusquedaCliente.html")






