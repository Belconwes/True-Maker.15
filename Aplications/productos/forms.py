from django.contrib.auth import forms
from django import forms
from django.forms import ModelForm
from .models import Producto


class Producto_f(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'