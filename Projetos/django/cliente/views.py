from django.shortcuts import render 

""" 
Criar uma pagina onde ele consiga visualizar os clientes cadastrados em formato de tabela

Vsualizar: 
Nome, Idade, Data_Nascimento

Dados devem vir de uma lista de dicionario
"""

def dados_clientes(request):
    titulo_pagina = "Dados dos clientes"

    #Lista - Dicionarios
    lista_clientes = [
        {'nome': 'Thyago Almeida', 'idade': '44 anos', 'nascimento': '15/02/1982'}, 
        {'nome': 'João Gabriel', 'idade': '18 anos', 'nascimento': '11/03/2007'},
        {'nome': 'Marcela Alves', 'idade': '20 anos', 'nascimento': '02/04/2005'},
        {'nome': 'Dilcimar Pinheiro', 'idade': '20 anos', 'nascimento': '02/04/2005'},        
    ]

    return render(request, 'clientes/dados_clientes.html', {'msg':titulo_pagina, 'lista': lista_clientes })