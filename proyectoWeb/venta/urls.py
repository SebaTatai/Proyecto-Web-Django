from django.urls import path
from . import views
from .views import CrudProducto_view

urlpatterns = [
    path('index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('registro2',views.registro2,name='registro2'),
    path('sec',views.sec,name='sec'),
    path('short1',views.short1,name='short1'),
    path('short2',views.short2,name='short2'),
    path('short3',views.short3,name='short3'),
    path('shortsH',views.shortsH,name='shortsH'),
    path('Administrador',views.lista_productos,name='Administrador'),
    path('AgregarProducto',views.AgregarProducto,name='AgregarProducto'),
    path('ListarProducto',views.ListarProducto,name='ListarProducto'),
    path('EliminarProducto/<str:pk',views.eliminar_productos,name='EliminarProducto'),


 
    
]

