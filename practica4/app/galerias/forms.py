from django import forms
from django.forms import widgets


from . import models

from django.forms.models import ModelForm





class GaleriaForm(ModelForm):
  class Meta:
    model = models.Galeria
    fields = ('nombre' , 'direccion',)
    widgets ={
        'nombre' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'nombre' }),
        'direccion' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'direccion' }),
    }
    
class CuadroForm(ModelForm):
  class Meta:
    model = models.Cuadro
    fields = '__all__'
    widgets ={
        'nombre' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'nombre' }),
        'autor' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'autor' }),
        'fechacreaion' : forms.DateInput(attrs={'class' : 'form-control'}),
    }



class ElegirGaleriaForm(forms.Form):
    galeria = forms.ModelMultipleChoiceField(queryset=models.Galeria.objects.all())


class ElegirCuadroForm(forms.Form):
    cuadro = forms.ModelMultipleChoiceField(queryset=models.Cuadro.objects.all())


