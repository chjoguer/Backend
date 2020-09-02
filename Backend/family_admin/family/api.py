from django.shortcuts import render
# Create your api rest here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import *
import json
import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework_jwt.views import ObtainJSONWebToken
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response

def get_temasPrincipales(request):
    if request.method=='GET':
        response = dict()
        temas = Tema.objects.all()
    
        for tema in temas:
            res = dict()
            response[tema.tema_categoria.nombre_categoria]= res
            res["Categoria"]=tema.tema_categoria.nombre_categoria
            res["Tema"]=tema.titulo
            imagenes = Imagenes_Tema.objects.filter(id_tema=tema.id_tema)[0]
            res["Imagen"]=imagenes.image.url
            print(imagenes.image.url)
            #response["img"]=usuario.imagen.url
        return JsonResponse(response)



