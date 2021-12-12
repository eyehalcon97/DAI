from django import forms
from django.db.models import fields
from django.forms import widgets
from . import models


class CuadroForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'nombre'}))
    galeria = forms.ModelMultipleChoiceField(queryset=models.Galeria.objects.all())
    autor = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'autor'}))
    fecha_creacion = forms.DateField(widget=forms.DateInput(),)
    
class GaleriaForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'nombre'}))
    direccion = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'direccion'}))

class EliminarGaleriaForm(forms.Form):
    galeria = forms.ModelMultipleChoiceField(queryset=models.Galeria.objects.all())


class EliminarCuadroForm(forms.Form):
    cuadro = forms.ModelMultipleChoiceField(queryset=models.Cuadro.objects.all())