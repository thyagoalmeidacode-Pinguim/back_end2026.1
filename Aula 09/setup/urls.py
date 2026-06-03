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
from cliente.views import dados_clientes, home #Chego na função criada na viewa

urlpatterns = [
    path('admin/', admin.site.urls),

    #Vai chamar a função ola_mundo dentro do views do app cliente
    #path('endereço/', metodo),
    path('', home, name='/'), #Em branco é a pagina home (Pagina padrao)
    path('dados/', dados_clientes, name="clientes")    
]