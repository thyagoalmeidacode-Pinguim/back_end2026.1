from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('abrir-conta/', views.abrir_conta, name='abrir_conta'),
    path('conta/<int:conta_id>/', views.conta, name='conta'),
    path('conta/<int:conta_id>/depositar/', views.depositar, name='depositar'),
    path('conta/<int:conta_id>/sacar/', views.sacar, name='sacar'),
    path('acessar_conta/', views.acessar_conta, name='acessar_conta'),
    path('sair/', views.sair, name='sair')
]