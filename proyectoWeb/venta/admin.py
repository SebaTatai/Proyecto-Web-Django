from django.contrib import admin
from .models import Usuario, Producto, Categoria, Carrito

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Carrito)

