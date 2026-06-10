from django.contrib import admin

# Importar nossos models.
#Dizer para o django quais sao nossas tabelas
from .models import Cliente, Conta

#Registrar nosso modelo no ambiente adminastrativo do django
admin.site.register(Cliente)
admin.site.register(Conta)