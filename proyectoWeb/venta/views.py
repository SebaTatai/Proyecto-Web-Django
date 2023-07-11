from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria 
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm
from django.db.models import Q
from venta.Carrito import Carrito


# Create your views here.
def index (request):
    return render(request, "venta/index.html")

def login (request):
    return render(request, "venta/login.html")

def registro2 (request):
    return render(request, "venta/registro2.html")

def poleraH1 (request):
    return render(request, "venta/poleraH1.html")

def poleraH2 (request):
    return render(request, "venta/poleraH2.html")

def poleraH3 (request):
    return render(request, "venta/poleraH3.html")

def poleraH (request):
    return render(request, "venta/poleraH.html")

def poleronesH (request):
    return render(request, "venta/poleronesH.html")

def sec (request):
    return render(request, "venta/sec.html")

def short1 (request):
    return render(request, "venta/short1.html")

def short2 (request):
    return render(request, "venta/short2.html")

def short3 (request):
    return render(request, "venta/short3.html")

def shortsH (request):
    return render(request, "venta/shortsH.html")

def AgregarProducto (request):
    return render(request, "AgregarProducto.html")

def ListarProducto (request):
    return render(request, "ListarProducto.html")

def Administrador (request):
    return render(request, "Administrador.html")

def EliminarProducto (request):
    return render(request, "EliminarProducto.html")

def AdministradorCategorias (request):
    return render(request, "venta/AdministradorCategorias.html")

def carrito (request):
    return render(request, "venta/carrito.html")









#Crud producto
@login_required
def inicio (request):
    request.session["usuario"]= "smorales"
    lista_productos = Producto.objects.all()
    lista_categorias = Categoria.objects.all()
    usuario = request.session ["usuario"]

    context={"productos":lista_productos,"usuario":usuario, "categorias":lista_categorias}
    return render(request, 'venta/Administrador.html', context)

def lista_productos(request):
    
    busqueda = request.GET.get("buscar")
    lista_productos = Producto.objects.raw("SELECT * FROM venta_Producto")

    if busqueda:
        lista_productos = Producto.objects.filter(
            Q(codigo_producto__icontains = busqueda) | 
            Q(nombre__icontains = busqueda)
        ).distinct()

    for producto in lista_productos:
        print(type(producto.codigo_producto))
        print(type(producto.codigo_categoria))
        print (producto)
    context={"productos":lista_productos}
    return render(request, 'venta/Administrador.html', context)

    

def lista_categorias(request):
    lista_categorias  = Categoria.objects.raw("SELECT * FROM venta_Categoria")
    for categoria in lista_categorias:
        print(type(categoria.codigo_categoria))
    context={"categorias":lista_categorias}
    return render(request, 'venta/AdministradorCategorias.html', context)

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
    
 
 #Eliminar producto crud x codigo_categoria.
@login_required
def eliminar_producto(request, codigo_producto):
    
    try:
        producto = Producto.objects.get(codigo_producto=codigo_producto)
        producto.delete() #delete en la BD
        mensaje = "Se eliminó el producto"
        lista_productos = Producto.objects.all()
        context={"productos":lista_productos, "mensaje":mensaje}
        return render(request,'venta/Administrador.html',context)
    except:
        mensaje = "No se eliminó el producto"
        lista_productos = Producto.objects.all()
        context={"productos":lista_productos, "mensaje":mensaje}
        return render(request,'venta/Administrador.html',context)    

#Modificar producto.
@login_required
def modificar_producto(request, codigo_producto):
    if request.method == "POST":
        codigo_producto = request.POST["codigo_producto"]
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        precio = request.POST["precio"]
        cantidad_stock = request.POST["cantidad_stock"]
        categoria = request.POST["categoria"]
       
        try:
            objCategoria = Categoria.objects.get(codigo_categoria=categoria)
            producto = Producto.objects.get(codigo_producto=codigo_producto)

            producto.nombre = nombre
            producto.descripcion = descripcion
            producto.precio = precio
            producto.cantidad_stock = cantidad_stock
            producto.codigo_categoria = objCategoria

            producto.save()
            mensaje = "Producto modificado correctamente"
        except Categoria.DoesNotExist:
            mensaje = "La categoría no existe"
        except Producto.DoesNotExist:
            mensaje = "El producto no existe"
        
        producto = Producto.objects.get(codigo_producto=codigo_producto)
        lista_categorias = Categoria.objects.all()
        context = {"mensaje": mensaje, "categorias": lista_categorias,"producto": producto}
        return render(request, 'venta/ModificarP.html', context)
    else:
        producto = Producto.objects.get(codigo_producto=codigo_producto)
        lista_categorias = Categoria.objects.all()
        context = {"categorias": lista_categorias, "producto": producto}
        return render(request, 'venta/ModificarP.html', context)

@login_required
def CrudProducto_view(request):
    return render(request, 'CrudProducto.html')



def index(request):
    productos = Producto.objects.all()
    return render(request, "venta/index.html", {'productos':productos})

def agregar_producto(request, codigo_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(codigo_producto=codigo_producto)
    carrito.agregar(producto)
    return redirect("carrito")

def eliminar_producto_carrito(request, codigo_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(codigo_producto=codigo_producto)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, codigo_producto):
    carrito = Carrito(request)
    producto = Producto.objects.get(codigo_producto=codigo_producto)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")

def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
    return render(request, "venta/index.html",{'total_carrito': total})


    

