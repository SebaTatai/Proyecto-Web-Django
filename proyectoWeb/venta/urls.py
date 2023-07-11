from django.urls import path
from . import views
from .views import CrudProducto_view, eliminar_producto, modificar_producto, lista_productos, lista_categorias

urlpatterns = [
    path('index',                      views.index,name='index'),
    path('carrito',                    views.carrito,name='carrito'),
    path('login',                      views.login,name='login'),
    path('registro2',                  views.registro2,name='registro2'),
    path('sec',                        views.sec,name='sec'),
    path('short1',                     views.short1,name='short1'),
    path('short2',                     views.short2,name='short2'),
    path('short3',                     views.short3,name='short3'),
    path('shortsH',                    views.shortsH,name='shortsH'),
    path('Administrador',              views.lista_productos,name='Administrador'),
    path('AdministradorCategorias',    views.lista_categorias,name='AdministradorCategorias'),
    path('AgregarProducto',            views.crear_producto,name='AgregarProducto'),
    path('ListarProducto',             views.ListarProducto,name='ListarProducto'),
    #path('EliminarProducto/<str:pk>',  views.eliminar_productos,name='EliminarProducto'),
    #path('ModificarProducto/<str:pk>', views.editar_producto,name='ModificarProducto'),
    
    
    path('eliminar-producto/<int:codigo_producto>/', views.eliminar_producto, name='eliminar_producto'),
    path('modificar-producto/<int:codigo_producto>/', views.modificar_producto, name="modificar_producto"),
    
    path('agregar/<int:codigo_producto>/', views.agregar_producto, name="Add"),
    path('eliminar/<int:codigo_producto>/', views.eliminar_producto, name="Del"),
    path('restar/<int:codigo_producto>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),
]

