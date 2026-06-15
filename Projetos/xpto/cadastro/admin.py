from django.contrib import admin

#Para exibir a base de dados dentro do ambiente administrativo
from .models import Aluno, Campus

admin.site.register(Aluno)
admin.site.register(Campus)