from django.shortcuts import render
from .models import Producto, Categoria 
from django.contrib.auth.decorators import login_required


# Create your views here.
def index (request):
    return render(request, "index.html")

def login (request):
    return render(request, "login.html")

def registro2 (request):
    return render(request, "registro2.html")

def poleraH1 (request):
    return render(request, "poleraH1.html")

def poleraH2 (request):
    return render(request, "poleraH2.html")

def poleraH3 (request):
    return render(request, "poleraH3.html")

def poleraH (request):
    return render(request, "poleraH.html")

def poleronesH (request):
    return render(request, "poleronesH.html")

def sec (request):
    return render(request, "sec.html")

def short1 (request):
    return render(request, "short1.html")

def short2 (request):
    return render(request, "short2.html")

def short3 (request):
    return render(request, "short3.html")

def shortsH (request):
    return render(request, "shortsH.html")

def AgregarProducto (request):
    return render(request, "AgregarProducto.html")

def ListarProducto (request):
    return render(request, "ListarProducto.html")

def Administrador (request):
    return render(request, "Administrador.html")

def EliminarProducto (request):
    return render(request, "EliminarProducto.html")






#Crud producto
@login_required
def inicio (request):
    request.session["usuario"]= "smorales"
    lista_productos = Producto.objects.all()
    usuario = request.session ["usuario"]

    context={"productos":lista_productos,"usuario":usuario}
    return render(request, 'venta/Administrador.html', context)

def lista_productos(request):
    lista_productos  = Producto.objects.raw("SELECT * FROM venta_Producto")
    context={"productos":lista_productos}
    return render(request, 'venta/Administrador.html', context)



@login_required
def crear_producto (request):
    if request.method != "POST":
        lista_categorias = Categoria.objects.all()
        context = {"categorias":lista_categorias}
        return render (request, 'venta/AgregarProducto.html', context)
    else:
        codigo_producto  = request.POST["codigo_producto"]
        nombre           = request.POST["nombre"]
        descripcion      = request.POST["descripcion"]
        precio           = request.POST["precio"]
        cantidad_stock   = request.POST["cantidad_stock"]
        categoria        = request.POST["categoria"]
       

        objCategoria = Categoria.objects.get(codigo_categoria = categoria)

        objProducto = Producto.objects.create(
            codigo_producto  = codigo_producto,
            nombre           = nombre,
            descripcion      = descripcion,
            precio           = precio,
            cantidad_stock   = cantidad_stock,
            codigo_categoria = objCategoria)

        objProducto.save()
        lista_categorias = Categoria.objects.all()
        context = {"mensaje": "Se guardo producto", "categorias":lista_categorias}
        return render (request, 'venta/AgregarProducto.html', context)

def eliminar_productos(request,pk):
    
    try:
        producto = Producto.objects.get(codigo_producto=pk)

        producto.delete() #delete en la BD
        mensaje = "Se eliminó producto"
        lista_productos = Alumno.objects.all()
        context={"productos":lista_productos, "mensaje":mensaje}
        return render(request,'venta/Administrador.html',context)
    except:
        mensaje = "No se eliminó producto"
        lista_productos = Producto.objects.all()
        context={"productos":lista_alumnos, "mensaje":mensaje}
        return render(request,'venta/Administrador.html',context)


@login_required
def editar_producto(request):
    if request.method == "POST":
        codigo_producto  = request.POST["codigo_producto"]
        nombre           = request.POST["nombre"]
        descripcion      = request.POST["descripcion"]
        precio           = request.POST["precio"]
        cantidad_stock   = request.POST["cantidad_stock"]
        categoria        = request.POST["categoria"]

        objCategoria = Categoria.objects.get(codigo_categoria = categoria)

        objProducto = Producto()
        objProducto.codigo_producto  = codigo_producto
        objProducto.nombre           = nombre
        objProducto.descripcion      = descripcion
        objProducto.precio           = precio
        objProducto.cantidad_stock   = cantidad_stock
        objProducto.codigo_categoria = objCategoria

        objProducto.save()
        lista_categorias = Categoria.objects.all()
        context = {"mensaje":"Se actualizó producto","categorias":lista_categorias}
        return render(request,'venta/ModificarProducto.html',context)

    else:
        lista_productos = Producto.objects.all()
        context = {"productos":lista_productos}
        return render(request,'venta/Administrador.html',context)


@login_required
def CrudProducto_view(request):
    return render(request, 'CrudProducto.html')



    

