from django.shortcuts import render 

#Conectar ao arquivo models. Importa a classe
from .models import Cliente, Conta

""" 
Criar uma pagina onde ele consiga visualizar os clientes cadastrados em formato de tabela

Vsualizar: 
Nome, Idade, Data_Nascimento

Dados devem vir de uma lista de dicionario
"""
def home(request):
    titulo = "Pagina Inicial"
    return render(request, 'clientes/home.html', {'titulo': titulo})

def dados_clientes(request):
    titulo = "Nossos Clientes" 
    #Tras todos os dadsos do model Cliente
    nossos_clientes = Cliente.objects.all() #Importa os dados do banco de dados
    return render(request, 'clientes/dados_clientes.html', {'titulo': titulo, 'dados_clientes':nossos_clientes})

def conta(request):
    titulo = "Contas Pessoas Físicas"
    nossas_contas = Conta.objects.all()
    return render(request, 'clientes/dados_contas.html', {'titulo': titulo, 'contas':nossas_contas})








def fomulario(request):
    titulo = "Cadastro Clientes"
    return render(request, 'clientes/form.html', {'titulo':titulo})

def contato(request):
    titulo = "Contato"
    contato = "email@python.com"
    return render(request, 'clientes/contato.html', {'titulo': titulo, 'contato': contato})
