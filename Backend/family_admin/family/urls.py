from django.urls import path
from .views import *
from .api import *

urlpatterns = [
     path('', signup),
     path('index', content, name ='index'),
     path('signup', signup, name='signup'),
     path('logout', logout_view, name='logout'),

     #tema
     path('tema', vista_registrar_tema, name='registrar_tema'),
     path('tema_modificar', view_modificar_tema, name='modificar_tema'),
     path('tema_modificar/<int:pk>', modificar_tema, name='modificar_tema_pk'),

     path('tema_eliminar', view_eliminar_tema, name='eliminar_tema'),
     path('tema_eliminar/<int:pk>', eliminar_tema, name='eliminar_tema_pk'),


     #galeria
     path('galeria', view_galeria, name='galeria'),
     path('galeria_eliminar', view_eliminar_galeria, name='hola'),
     path('galeria_eliminar_pk/<int:pk>', eliminar_galeria, name='eliminar_galeriaPK'),


     path('buzon', vista_buzon_entrada, name='buzon_entrada'),

     #Api para el consumo en el frontend
     path('getPrincipalesTemas/', get_temasPrincipales),



     
]