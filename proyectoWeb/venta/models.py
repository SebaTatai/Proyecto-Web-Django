from django.db import models

class Producto(models.Model):
    codigo_producto  = models.CharField(db_column='codigoProducto', primary_key=True, max_length=25)
    nombre           = models.CharField(max_length=25)
    descripcion      = models.CharField(max_length=300)
    precio           = models.IntegerField()
    cantidad_stock   = models.CharField(max_length=25)
    codigo_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, db_column='codigoCategoria')
    imagen           = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.nombre) + " - " + str(self.codigo_producto)

class Usuario(models.Model):
    rut              = models.CharField(db_column='rutUsuario', primary_key=True, max_length=12)
    nombre           = models.CharField(max_length=25)
    apellido_paterno = models.CharField(max_length=25)
    apellido_materno = models.CharField(max_length=25)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    correo           = models.EmailField(unique=True, max_length=110, blank=False, null=False)
    direccion        = models.CharField(max_length=55, blank=False, null=False)

    def __str__(self):
        return str(self.nombre)+ " " + str(self.apellido_paterno) + " " + str(self.apellido_materno) + " - " + str(self.rut)

class Categoria(models.Model):
    codigo_categoria = models.IntegerField(db_column='codigoCategoria', primary_key=True)
    categoria        = models.CharField(max_length=10)

    def __str__(self):
        return str(self.codigo_categoria) + " - " + str(self.categoria) 

class Carrito(models.Model):
    codigo_carrito  = models.IntegerField(db_column='codigoCarrito', primary_key=True)
    rut             = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='rutUsuario')
    codigo_producto = models.ForeignKey('Producto', on_delete=models.CASCADE, db_column='codigoProducto')
    cantidad        = models.IntegerField()
    producto        = models.CharField(max_length=25)
    estado          = models.CharField(max_length=10, null=False)

    def __str__(self):
        return str(self.codigo_carrito) + " " + str(self.rut)





    







