# mi_aplicacion/views.py

import logging

from django.db.models.deletion import RestrictedError
from django.http.request import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from django.template import Template, Context, loader
from django.middleware import csrf
from django.http import JsonResponse
from os import remove


from . import forms
from . import models



def index(request):
    if request.user.is_authenticated:
        return HttpResponse( render( request, 'base.html', {'username':request.user } ) )
    return render(request, 'base.html')

def ejemplo(request):
        return render(request,'ejemplo.html')

def VerGalerias(request):
    lista_galerias = models.Galeria.objects.all()
    formcreargaleria = forms.GaleriaForm


    if request.user.is_authenticated:
        return HttpResponse( render( request, 'verGalerias.html', { 'galerias': lista_galerias , 'formcreargaleria': formcreargaleria , 'username':request.user  } ) )
    return HttpResponse( render( request, 'verGalerias.html', { 'galerias': lista_galerias ,'formcreargaleria': formcreargaleria  } ))



def VerCuadros(request):
    lista_cuadros = models.Cuadro.objects.all()
    formcrearcuadro = forms.CuadroForm

    if request.user.is_authenticated:
        return HttpResponse( render( request, 'verCuadros.html', {  'cuadros' : lista_cuadros ,'formcrearcuadro':formcrearcuadro, 'username':request.user  } ) )
    return HttpResponse( render( request, 'verCuadros.html', {  'cuadros' : lista_cuadros ,'formcrearcuadro':formcrearcuadro} ))



def CrearGaleria(request):
    if request.method == 'POST':
        formulario = forms.GaleriaForm(request.POST)
        #print (request.POST['nombre'])
        if formulario.is_valid():
            formulario.save()
    return HttpResponseRedirect('/VerGalerias')



def CrearCuadro(request):
    if request.method == 'POST':
        formulario = forms.CuadroForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
    return HttpResponseRedirect('/VerCuadros')

def EliminarGaleria(request, numero):
    if request.method == 'DELETE':
        galeria = models.Galeria.objects.get(id=numero)
        galeria.delete()
    return HttpResponseRedirect('/VerGalerias')

def EliminarCuadro(request, numero):
    if request.method == 'DELETE':
        cuadro = models.Cuadro.objects.get(id=numero)
        cuadro.imagen.delete()
        cuadro.delete()
    return HttpResponseRedirect('/VerCuadros')



def ModificarFormularioGaleria(request, numero):
    if request.method == 'GET':
        galeria = models.Galeria.objects.get(id=numero)
        formulario = str(forms.GaleriaForm(instance=galeria))
        
        return HttpResponse(formulario)


def ModificarFormularioCuadro(request, numero):
    if request.method == 'GET':
        cuadro = models.Cuadro.objects.get(id=numero)
        formulario = str(forms.CuadroForm(instance=cuadro))
        
        return HttpResponse(formulario)


def EditarGaleria(request,numero):
    if request.method == 'POST':
        galeria = models.Galeria.objects.get(id = numero)
        formulario = forms.GaleriaForm(request.POST,instance=galeria)
        if formulario.is_valid():
            formulario.save()
        else:
            
            print("no valido")
    print("fuera")
    return HttpResponseRedirect('/VerGalerias')

def EditarCuadro(request,numero):
    if request.method == 'POST':
        cuadro = models.Cuadro.objects.get(id = numero)
        formulario = forms.CuadroForm(request.POST,instance=cuadro)
        if formulario.is_valid():
            formulario.save()
    return HttpResponseRedirect('/VerCuadros')






