from django.shortcuts import render, redirect, get_object_or_404
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
    usuario = request.session ["usuario"]
    context = {'usuario':usuario}
    return render(request, 'Administrador.html', context)


@login_required
def lista_productos(request):
    lista_productos  = Producto.objects.raw("SELECT * FROM venta_Producto")
    context={"productos":lista_productos}
    return render(request, 'Administrador.html', context)



@login_required
def crear_producto (request):
    if request.method != "POST":
        lista_categorias = Categoria.objects.all()
        context = {"categorias":lista_categorias}
        return render (request, 'venta/Administrador.html', context)
    else:
        nombre           = request.POST["nombre"]
        descripcion      = request.POST.get('descripcion')
        precio           = request.POST.get('precio')
        cantidad_stock   = request.POST.get('cantidad_stock')
        codigo_categoria = request.POST.get('codigo_categoria')
        codigo_producto  = request.POST.get('codigo_producto')

        objCategoria = Categoria.objects.get(codigo_categoria = categoria)

        objProducto = Producto.objects.create(
            nombre           = nombre,
            descripcion      = descripcion,
            precio           = precio,
            cantidad_stock   = cantidad_stock,
            codigo_categoria = objCategoria,
            codigo_producto  = codigo_producto)

        objProducto.save()
        lista_categorias = Categoria.objects.all()
        context = {"mensaje": "Se guardo producto", "categorias":lista_categorias}
        return render (request, 'venta/CrudProducto.html', context)

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
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        
        
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.precio = precio
        
        
        producto.save()
        
        return redirect('productos:lista_productos')
    
    return render(request, 'productos/editar_producto.html', {'producto': producto})



@login_required
def CrudProducto_view(request):
    return render(request, 'CrudProducto.html')



    

