from .models import Categoria, Producto
from django.forms import ModelForm
from django import forms

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ["categoria",]
        labels = {"categoria":"Categoria",}

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'