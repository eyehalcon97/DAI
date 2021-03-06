# galerias/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url



urlpatterns = [
    path('', views.index, name='home'),
    path('ejemplo', views.ejemplo, name='ejemplo'),
    path('VerGalerias', views.VerGalerias, name='VerCuadros'),
    path('VerCuadros', views.VerCuadros, name='VerGalerias'),
    path('CrearCuadro', views.CrearCuadro, name='CrearCuadro'),
    path('CrearGaleria', views.CrearGaleria, name='CrearGaleria'),
    path('EliminarGaleria/<int:numero>',views.EliminarGaleria, name='EliminarGaleria'),
    path('EliminarCuadro/<int:numero>',views.EliminarCuadro, name='EliminarCuadro'),
    path('EditarGaleria/<int:numero>',views.EditarGaleria, name='EditarGaleria'),
    path('EditarCuadro/<int:numero>',views.EditarCuadro, name='EditarCuadro'),
    path('ModificarFormularioGaleria/<int:numero>',views.ModificarFormularioGaleria, name='ModificarFormularioGaleria'),
    path('ModificarFormularioCuadro/<int:numero>',views.ModificarFormularioCuadro, name='ModificarFormularioCuadro'),

    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
