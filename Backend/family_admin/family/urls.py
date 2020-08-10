from django.urls import path
from .views import *

urlpatterns = [
     path('', signup),
     path('index', index),
     path('signup', signup, name='signup'),
     path('logout', logout, name='logout'),
]