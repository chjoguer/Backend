from django.urls import path
from .views import *
from .api import *
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [

     path('', signup),
     path('index', content, name ='index'),
     path('signup', signup, name='signup'),
     path('logout', logout_view, name='logout'),
     path('recuperar-password', forgot_password,name='password'),#template
     path('recuperar_contrasenia', recuperar_contrasenia,name='reset_pass'),#method
     #tema
     path('tema', vista_registrar_tema, name='registrar_tema'),
     path('tema_modificar', view_modificar_tema, name='modificar_tema'),
     path('tema_modificar/<int:pk>', modificar_tema, name='modificar_tema_pk'),

     path('tema_eliminar', view_eliminar_tema, name='eliminar_tema'),
     path('eliminar_tema_p', eliminar_tema_p, name='eliminar_tema_p'),


     #galeria
     path('galeria', view_galeria, name='galeria'),
     path('galeria_eliminar', view_eliminar_galeria, name='hola'),
     path('eliminar_galeria_pk', eliminar_galeria, name='eliminar_galeria_p'),


     path('buzon', vista_buzon_entrada, name='buzon_entrada'),

    
     path('recibir_imagenes', recibir_imagenes),
     path('recibir_video', recibir_video, name='recibir_video'),


     #Api para el consumo en el frontend
     path('getPrincipalesTemas/', get_temasPrincipales),
     
     #autenticacion
    
    path('api-token-auth/', obtain_jwt_token),
     path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]