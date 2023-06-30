from .models import Gategoria, Producto
from django.forms import ModelForm

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ["categoria",]
        labels = {"categoria":"Categoria",}

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ["producto",]
        labels = {"producto":"Producto",}