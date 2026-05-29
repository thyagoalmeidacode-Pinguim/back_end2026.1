"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#Diz para o urls onde encontrar a função ola_mundo
from cliente.views import ola_mundo, contato, home, formulario

urlpatterns = [
    path('admin/', admin.site.urls),

    #Vai chamar a função ola_mundo dentro do views do app cliente
    #path('endereço/', metodo), 
    path('ola/', ola_mundo),
    path('contato_form/', contato),

    
    path('inicio/', home),
    path('cadastro/', formulario)
]