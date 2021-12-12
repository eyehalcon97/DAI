# galerias/models.py
from django.db import models
from django.forms.models import ModelForm
from django.utils import timezone

class Galeria(models.Model):
  nombre     = models.CharField(max_length=200, primary_key=True)
  direccion  = models.CharField(max_length=100)

  
  def __str__(self):
    return self.nombre
  
  def hola(self):
    return self.nombre
  
  
class Cuadro(models.Model):
  nombre           = models.CharField(max_length=100,primary_key= True)
  galeria          = models.ForeignKey('Galeria', on_delete=models.CASCADE)
  autor            = models.CharField(max_length=100)
  fecha_creacion   = models.DateField(default=timezone.now)
  
  
  def __str__(self):
    return self.nombre


class GaleriaForm(ModelForm):
  class Meta:
    model = Galeria
    fields = ('nombre' , 'direccion',)
    
class CuadroForm(ModelForm):
  class Meta:
    model = Cuadro
    fields = '__all__'

