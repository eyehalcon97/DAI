# galerias/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='home'),
    path('Ver', views.Ver, name='Ver'),
    path('CrearCuadro', views.CrearCuadro, name='CrearCuadro'),
    path('CrearGaleria', views.CrearGaleria, name='CrearGaleria'),
    path('EliminarGaleria',views.EliminarGaleria, name='EliminarGaleria'),
    path('EliminarCuadro',views.EliminarCuadro, name='EliminarCuadro'),
    path('ElegirModificarGaleria',views.ElegirModificarGaleria, name='ElegirModificarGaleria'),
    path('ModificarGaleria/<int:numero>',views.ModificarGaleria, name='ModificarGaleria'),
    path('ElegirModificarCuadro',views.ElegirModificarCuadro, name='ElegirModificarCuadro'),
    path('ModificarCuadro/<int:numero>',views.ModificarCuadro, name='ModificarCuadro'),
    
]
