from django.contrib import admin
#Faz o import do model
from .models import Cliente

#Registra no ambiente administrativo
admin.site.register(Cliente)