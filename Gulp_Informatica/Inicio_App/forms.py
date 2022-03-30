from django import forms


class TrabajosForm(forms.Form):
# campos del formulario
    nombre_producto = forms.CharField(max_length=40)
    precio_instalacion = forms.IntegerField()
    cliente = forms.CharField(max_length=40)

class VentasForm(forms.Form):

    producto = forms.CharField(max_length=40)
    valor_producto = forms.IntegerField()
    precio_producto = forms.IntegerField() 

class PedidosForm(forms.Form):
    producto = forms.CharField(max_length=40)
    precio = forms.IntegerField()
    cliente = forms.CharField(max_length=40)