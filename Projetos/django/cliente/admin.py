from django.contrib import admin

# Importar nossos models.
#Dizer para o django quais sao nossas tabelas
from .models import Cliente

#Registrar nosso modelo no ambiente adminastrativo do django
admin.site.register(Cliente)