from django.contrib import admin
#Faz o import do model
from .models import Cliente, Conta, Movimento

#Registra no ambiente administrativo
admin.site.register(Cliente)
admin.site.register(Conta)
admin.site.register(Movimento)