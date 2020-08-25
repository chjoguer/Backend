from django.urls import path
from .views import *

urlpatterns = [
     path('', signup),
     path('index', content, name ='index'),
     path('signup', signup, name='signup'),
     path('logout', logout_view, name='logout'),


     path('tema', vista_registrar_tema, name='registrar_tema'),
     path('tema_modificar', view_modificar_tema, name='modificar_tema'),
     path('tema_modificar/<int:pk>', modificar_tema, name='modificar_tema'),

     path('galeria', view_galeria, name='galeria'),

     path('tema_eliminar', view_eliminar_tema, name='eliminar_tema'),
     path('tema_eliminar/<int:pk>', eliminar_tema, name='eliminar_tema_pk'),


     path('buzon', vista_buzon_entrada, name='buzon_entrada'),


     
]