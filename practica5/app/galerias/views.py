# mi_aplicacion/views.py

from django.db.models.deletion import RestrictedError
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from django.template import Template, Context, loader
from django.middleware import csrf
from os import remove
from . import forms
from . import models


def index(request):
    if request.user.is_authenticated:
        return HttpResponse( render( request, 'base.html', {'username':request.user } ) )
    return render(request, 'base.html')



def Ver(request):
    lista_galerias = models.Galeria.objects.all()
    lista_cuadros = models.Cuadro.objects.all()
    if request.user.is_authenticated:
        return HttpResponse( render( request, 'ver.html', { 'galerias': lista_galerias , 'cuadros' : lista_cuadros , 'username':request.user  } ) )
    return HttpResponse( render( request, 'ver.html', { 'galerias': lista_galerias , 'cuadros' : lista_cuadros } ))


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
    if request.user.is_superuser:
        if request.method == 'POST':
            formulario = forms.GaleriaForm(request.POST)
            if formulario.is_valid():
                formulario.save()
                msg = "Se ha creado la galeria"
            else:
                msg = "Error al crer la galeria"
            return HttpResponse( render( request, 'base.html', {'username':request.user , 'msg': msg } ) )
        else:   
            form = forms.GaleriaForm
            return HttpResponse(render(request, 'formularioCrear.html', {'form': form , 'username':request.user  }))
    else:
        msg = "No tienes permisos para realizar esta accion"
        if request.user.is_authenticated:
            return HttpResponse( render( request, 'base.html', {'username':request.user , 'msg': msg } ) )
        else:
            return HttpResponse( render( request, 'base.html', {'msg': msg } ) )


def EliminarGaleria(request):
    if request.user.is_superuser:    
        if request.method == 'POST':
            formulario = forms.ElegirGaleriaForm(request.POST)
            if formulario.is_valid():
                numero = request.POST.get('galeria')
                galeria = models.Galeria.objects.get(id = numero)
                galeria.delete()
                msg = "La galeria ha sido borrada"
            else:
                msg = "Error al borrar la galeria"
            return HttpResponse( render( request, 'base.html', {'username':request.user , 'msg': msg } ) )
        else:
            if len(models.Galeria.objects.all()) == 0:
                msg = "No hay Galerias creadas"
                form = ""
            else:
                msg = "Cual de las siguientes galerias desea modificar"   
                form = forms.ElegirGaleriaForm()
            return HttpResponse(render(request, 'formularioEliminar.html', {'form': form , 'msg': msg , 'username':request.user }))
    else:
        msg = "No tienes permisos para realizar esta accion"
        if request.user.is_authenticated:
            return HttpResponse( render( request, 'base.html', {'username':request.user , 'msg': msg } ) )
        else:
            return HttpResponse( render( request, 'base.html', {'msg': msg } ) )


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


def ElegirModificarGaleria(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            formulario = forms.ElegirGaleriaForm(request.POST)
            if formulario.is_valid():
                numero = request.POST.get('galeria')
                galeria = models.Galeria.objects.get(id=numero)
                url = '/ModificarGaleria/' + str(galeria.id)
                return HttpResponseRedirect(url)
            else:
                msg = "Error al modificar la galeria"
                return HttpResponse(render(request, 'base.html', { 'msg': msg , 'username':request.user }))
        else:
            if len(models.Galeria.objects.all()) == 0:
                msg = "No hay Galerias creadas"
                form = ""
            else:
                msg = "Cual de las siguientes galerias desea modificar"   
                form = forms.ElegirGaleriaForm()
            return HttpResponse(render(request, 'formularioModificar.html', {'form': form , 'msg': msg , 'username':request.user }))
    else:
        msg = "No tienes permisos para realizar esta accion"
        if request.user.is_authenticated:
            return HttpResponse( render( request, 'base.html', {'username':request.user , 'msg': msg } ) )
        else:
            return HttpResponse( render( request, 'base.html', {'msg': msg } ) )


def ElegirModificarCuadro(request):
    if request.user.is_staff:
        if request.method == 'POST':
            formulario = forms.ElegirCuadroForm(request.POST)
            if formulario.is_valid():
                numero = request.POST.get('cuadro')
                cuadro = models.Cuadro.objects.get(id = numero)
                url = '/ModificarCuadro/' + str(cuadro.id)
                return HttpResponseRedirect(url)
            else:
                msg = "Error al modificar el cuadro"
                return HttpResponse(render(request, 'base.html', { 'msg': msg , 'username':request.user }))
        else:
            if len(models.Cuadro.objects.all()) == 0:
                msg = "No hay Cuadros creados"
                form = ""
            else:
                msg = "Cual de los siguientes cuadros desea modificar"   
                form = forms.ElegirCuadroForm()
            return HttpResponse(render(request, 'formularioModificar.html', {'form': form , 'msg': msg , 'username':request.user }))
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


def ModificarGaleria(request, numero):
    if request.user.is_superuser:
        galeria = models.Galeria.objects.get(id = numero)
        if request.method == 'POST':
            formulario = forms.GaleriaForm(request.POST,instance=galeria)
            if formulario.is_valid():
                formulario.save()
                msg = "La galeria ha sido modificada con exito"
            else:
                msg = "Error al modificar la galeria"
            return HttpResponse(render(request, 'base.html', { 'msg': msg , 'username':request.user }))
        else:   
            form = forms.GaleriaForm(instance=galeria)
            return HttpResponse(render(request, 'formularioModificar.html', {'form': form  , 'username':request.user }))#
    else:
        msg = "No tienes permisos para realizar esta accion"
        if request.user.is_authenticated:
            return HttpResponse( render( request, 'base.html', {'username':request.user , 'msg': msg } ) )
        else:
            return HttpResponse( render( request, 'base.html', {'msg': msg } ) )
