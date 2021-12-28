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
    if request.method == 'POST':
        return render(request,'ejemplo.html')

def VerGalerias(request):
    lista_galerias = models.Galeria.objects.all()
    formcreargaleria = forms.GaleriaForm


    if request.user.is_authenticated:
        return HttpResponse( render( request, 'verGalerias.html', { 'galerias': lista_galerias , 'formcreargaleria': formcreargaleria , 'username':request.user  } ) )
    return HttpResponse( render( request, 'verGalerias.html', { 'galerias': lista_galerias ,'formcreargaleria': formcreargaleria  } ))



def VerCuadros(request):
    lista_cuadros = models.Cuadro.objects.all()

    if request.user.is_authenticated:
        return HttpResponse( render( request, 'verCuadros.html', {  'cuadros' : lista_cuadros , 'username':request.user  } ) )
    return HttpResponse( render( request, 'verCuadros.html', {  'cuadros' : lista_cuadros } ))



def CrearCuadro(request):
    if request.user.is_staff:
        if request.method == 'POST':
            formulario = forms.CuadroForm(request.POST, request.FILES)
            if formulario.is_valid():
                formulario.save()
                msg = "Se ha creado el cuadro"
            else:
                msg = "Error al crear el cuadro"
            return HttpResponse( render( request, 'base.html', {'username':request.user , 'msg': msg } ) )
        else:   
            form = forms.CuadroForm()
            return HttpResponse(render(request, 'formularioCrear.html', {'form': form , 'username':request.user }))
    else:
        msg = "No tienes permisos para realizar esta accion"
        if request.user.is_authenticated:
            return HttpResponse( render( request, 'base.html', {'username':request.user , 'msg': msg } ) )
        else:
            return HttpResponse( render( request, 'base.html', {'msg': msg } ) )
    

def CrearGaleria(request):
    if request.method == 'POST':
        formulario = forms.GaleriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
    return HttpResponseRedirect('/VerGalerias')


def EliminarGaleria(request, numero):
    if request.method == 'DELETE':
        galeria = models.Galeria.objects.get(id=numero)
        galeria.delete()
    return HttpResponseRedirect('/VerGalerias')



def ModificarFormularioGaleria(request, numero):
    if request.method == 'GET':
        galeria = models.Galeria.objects.get(id=numero)
        formulario = forms.GaleriaForm(instance=galeria)
        
        return HttpResponse(formulario)


def EditarGaleria(request,numero):
    if request.method == 'POST':
        galeria = models.Galeria.objects.get(id = numero)
        formulario = forms.GaleriaForm(request.POST,instance=galeria)
        if formulario.is_valid():
            print("entro")
            formulario.save()
        else:
            
            print("no valido")
    print("fuera")
    return HttpResponseRedirect('/VerGalerias')










def EliminarCuadro(request):
    if request.user.is_staff:
        if request.method == 'POST':
            formulario = forms.ElegirCuadroForm(request.POST)
            if formulario.is_valid():
                numero = request.POST.get('cuadro')
                cuadro = models.Cuadro.objects.get(id = numero)
                cuadro.imagen.delete()
                cuadro.delete()
                msg = "El cuadro ha sido borrado"
            else:
                msg = "Error al borrar el cuadro"
            return HttpResponse( render( request, 'base.html', {'username':request.user , 'msg': msg } ) )
        else:
            if len(models.Cuadro.objects.all()) == 0:
                msg = "No hay cuadros creados"
                form = ""
            else:
                msg = "Cual de los siguientes cuadros desea eliminar"  
                form = forms.ElegirCuadroForm()
            return HttpResponse(render(request, 'formularioEliminar.html', {'form': form , 'msg': msg , 'username':request.user }))
    else:
        msg = "No tienes permisos para realizar esta accion"
        if request.user.is_authenticated:
            return HttpResponse( render( request, 'base.html', {'username':request.user , 'msg': msg } ) )
        else:
            return HttpResponse( render( request, 'base.html', {'msg': msg } ) )




def ModificarCuadro(request,numero):
    if request.user.is_staff:
        cuadro = models.Cuadro.objects.get(id = numero)
        if request.method == 'POST':
            formulario = forms.CuadroForm(request.POST,instance=cuadro)
            if formulario.is_valid():
                formulario.save()
                msg = "El cuadro ha sido modificado"
            else:
                msg = "Error al modificar el cuadro"
            return HttpResponse(render(request, 'base.html', { 'msg': msg , 'username':request.user }))
        else:
            form = forms.CuadroForm(instance=cuadro)
            return HttpResponse(render(request, 'formularioModificar.html', {'form': form , 'username':request.user }))
    else:
        msg = "No tienes permisos para realizar esta accion"
        if request.user.is_authenticated:
            return HttpResponse( render( request, 'base.html', {'username':request.user , 'msg': msg } ) )
        else:
            return HttpResponse( render( request, 'base.html', {'msg': msg } ) )


