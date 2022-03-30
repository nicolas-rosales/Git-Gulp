from django.contrib import admin
from .models import *

# aca se registran los modelos

admin.site.register(Ventas)
admin.site.register(Trabajos)
admin.site.register(Pedidos)

