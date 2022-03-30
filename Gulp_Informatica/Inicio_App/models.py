from django.db import models

class Pedidos(models.Model):
    producto = models.CharField(max_length=40)
    precio = models.IntegerField()
    cliente = models.CharField(max_length=40)
    
class Trabajos(models.Model):
    nombre_producto = models.CharField(max_length=40)
    precio_instalacion = models.IntegerField()
    cliente = models.CharField(max_length=40)

    
class Ventas(models.Model):
    producto = models.CharField(max_length=40)
    valor_producto = models.IntegerField()
    precio_producto = models.IntegerField()
