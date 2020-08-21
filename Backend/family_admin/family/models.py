from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

#class customUser(AbstractUser):
#   rol = models.CharField(max_length=2,default='e')#A: administrador, E:editor, C:consejero


class UserProfile(AbstractUser):
    customer_id = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.CharField(max_length=2,null=False,blank=False,default='E',verbose_name='Tipos de usuario')# A:administrador, E: editor, C: consejero

    def say_hello(self):
        return "Hello, my name is {}".format(self.first_name)


class Cart(models.Model):
   user = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                null=True, blank=True, on_delete=models.CASCADE)
