from django.contrib import admin
from .models import Cliente, Conta, Movimento

admin.site.register(Cliente)    
admin.site.register(Conta)
admin.site.register(Movimento)
# Register your models here.
