# mi_aplicacion/views.py

from django.db.models.deletion import RestrictedError
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from django.template import Template, Context, loader
from django.middleware import csrf
from . import forms
from . import models


def index(request):
    pagina = loader.get_template("base.html")
    solucion = pagina.render()
    return HttpResponse(solucion)

def Ver(request):
    lista_galerias = models.Galeria.objects.all()
    lista_cuadros = models.Cuadro.objects.all()
    solucion = render( request, 'ver.html', { 'galerias': lista_galerias , 'cuadros' : lista_cuadros } )
    return HttpResponse( solucion )


def CrearCuadro(request):
    if request.method == 'POST':
       formulario = forms.CuadroForm(request.POST, request.FILES)
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
       formulario = forms.GaleriaForm(request.POST)
       if formulario.is_valid():
            formulario.save()
            
            return HttpResponse("Se ha guardado correctamente la galeria")
       else:
            lista = models.Galeria.objects.values()
            return HttpResponse(lista)
    else:   
        form = forms.GaleriaForm
        solucion = render(request, 'formularioCrear.html', {'form': form})
        return HttpResponse(solucion)
    
def EliminarGaleria(request):
    if request.method == 'POST':
        formulario = forms.ElegirGaleriaForm(request.POST)
        if formulario.is_valid():
            numero = request.POST.get('galeria')
            galeria = models.Galeria.objects.get(id = numero)
            galeria.delete()
            return HttpResponse("Se ha eliminado correctamente")
        return HttpResponse("no valido")
    else:
        if len(models.Galeria.objects.all()) == 0:
            msg = "No hay Galerias creadas"
            form = ""
        else:
            msg = "Cual de las siguientes galerias desea modificar"   
            form = forms.ElegirGaleriaForm()
        solucion = render(request, 'formularioEliminar.html', {'form': form , 'msg': msg})
        return HttpResponse(solucion)

def EliminarCuadro(request):
    if request.method == 'POST':
        formulario = forms.ElegirCuadroForm(request.POST)
        if formulario.is_valid():
            numero = request.POST.get('cuadro')
            cuadro = models.Cuadro.objects.get(id = numero)
            cuadro.delete()
            return HttpResponse("Se ha eliminado correctamente")
        return HttpResponse("no valido")
    else:
        if len(models.Cuadro.objects.all()) == 0:
            msg = "No hay cuadros creados"
            form = ""
        else:
            msg = "Cual de los siguientes cuadros desea eliminar"  
            form = forms.ElegirCuadroForm()
        solucion = render(request, 'formularioEliminar.html', {'form': form , 'msg' : msg})
        return HttpResponse(solucion)



def ElegirModificarGaleria(request):
    if request.method == 'POST':
        formulario = forms.ElegirGaleriaForm(request.POST)
        if formulario.is_valid():
            numero = request.POST.get('galeria')
            galeria = models.Galeria.objects.get(id=numero)
            url = '/ModificarGaleria/' + str(galeria.id)
            return HttpResponseRedirect(url)
        return HttpResponse("no valido")
    else:
        if len(models.Galeria.objects.all()) == 0:
            msg = "No hay Galerias creadas"
            form = ""
        else:
            msg = "Cual de las siguientes galerias desea modificar"   
            form = forms.ElegirGaleriaForm()
        solucion = render(request, 'formularioModificar.html', {'form': form , 'msg' : msg})
        return HttpResponse(solucion)

def ElegirModificarCuadro(request):
    if request.method == 'POST':
        formulario = forms.ElegirCuadroForm(request.POST)
        if formulario.is_valid():
            numero = request.POST.get('cuadro')
            cuadro = models.Cuadro.objects.get(id = numero)
            url = '/ModificarCuadro/' + str(cuadro.id)
            return HttpResponseRedirect(url)
        return HttpResponse("no valido")
    else:
        if len(models.Cuadro.objects.all()) == 0:
            msg = "No hay Cuadros creados"
            form = ""
        else:
            msg = "Cual de los siguientes cuadros desea modificar"   
            form = forms.ElegirCuadroForm()
        solucion = render(request, 'formularioModificar.html', {'form': form , 'msg' : msg})
        return HttpResponse(solucion)

def ModificarCuadro(request,numero):
    cuadro = models.Cuadro.objects.get(id = numero)
    if request.method == 'POST':
       formulario = forms.CuadroForm(request.POST,instance=cuadro)
       if formulario.is_valid():
            formulario.save()
            lista = models.Cuadro.objects.all()
            return HttpResponse(lista)
       else:
            lista = models.Cuadro.objects.values()
            return HttpResponse(lista)
    else:
        form = forms.CuadroForm(instance=cuadro)
        solucion = render(request, 'formularioModificar.html', {'form': form})
        return HttpResponse(solucion)



def ModificarGaleria(request, numero):
    galeria = models.Galeria.objects.get(id = numero)
    if request.method == 'POST':
       formulario = forms.GaleriaForm(request.POST,instance=galeria)
       if formulario.is_valid():
            formulario.save()
            lista = models.Galeria.objects.all()
            return HttpResponse(lista)
       else:
            lista = models.Galeria.objects.values()
            return HttpResponse(lista)
    else:   
        form = forms.GaleriaForm(instance=galeria)
        solucion = render(request, 'formularioModificar.html', {'form': form})
        return HttpResponse(solucion)
