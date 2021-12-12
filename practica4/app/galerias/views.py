# mi_aplicacion/views.py

from django.db.models.deletion import RestrictedError
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from django.template import Template, Context, loader
from django.middleware import csrf
from . import forms
from . import models


def index(request):
    pagina = loader.get_template("index.html")
    solucion = pagina.render()
    return HttpResponse(solucion)

def Ver(request):
    pagina = loader.get_template("index.html")
    solucion = pagina.render()
    return HttpResponse("hola")


def CrearCuadro(request):
    if request.method == 'POST':
       formulario = models.CuadroForm(request.POST, request.FILES)
       if formulario.is_valid():
            formulario.save()
            lista = models.Cuadro.objects.values()
            return HttpResponse(lista)
       else:
            lista = models.Cuadro.objects.all()
            return HttpResponse("no valido")

    else:   
        form = forms.CuadroForm()
        solucion = render(request, 'formularioCrear.html', {'form': form})
        return HttpResponse(solucion)
    
    

def CrearGaleria(request):
    if request.method == 'POST':
       formulario = models.GaleriaForm(request.POST)
       if formulario.is_valid():
            formulario.save()
            
            return HttpResponse("Se ha guardado correctamente la galeria")
       else:
            lista = models.Galeria.objects.values()
            return HttpResponse(lista)
    else:   
        form = forms.GaleriaForm()
        solucion = render(request, 'formularioCrear.html', {'form': form})
        return HttpResponse(solucion)
    
def EliminarGaleria(request):
    if request.method == 'POST':
        formulario = forms.EliminarGaleriaForm(request.POST)

        #datos = formulario.cleaned_data['galeria']
            #galeria = models.Galeria.objects.get(nombre = 'formulario["galeria"]')
        return HttpResponse(formulario)
        return HttpResponse("no valido")
    else:   
        form = forms.EliminarGaleriaForm()
        solucion = render(request, 'formularioEliminar.html', {'form': form})
        return HttpResponse(solucion)

def EliminarCuadro(request):
    if request.method == 'POST':
        formulario = ""
        return None
    else:   
        form = forms.EliminarCuadroForm()
        solucion = render(request, 'formularioEliminar.html', {'form': form})
        return HttpResponse(solucion)

def ModificarGaleria(request):
    if request.method == 'POST':
        formulario = ""
        return None
    else:   
        form = forms.GaleriaForm()
        solucion = render(request, 'formularioCrear.html', {'form': form})
        return HttpResponse(solucion)

def ModificarCuadro(request):
    if request.method == 'POST':
        formulario = ""
        return None
    else:   
        form = forms.GaleriaForm()
        solucion = render(request, 'formularioCrear.html', {'form': form})
        return HttpResponse(solucion)