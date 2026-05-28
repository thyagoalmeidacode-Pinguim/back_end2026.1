from django.shortcuts import render #Ja vem por padrão

#Importar a classe (Ferramenta) HttpResponse
from django.http import HttpResponse #Vai responder a solicitação do navegador

#Cria a função que reposnde a solicitação do navegador
def ola_mundo(request):
    return HttpResponse("<h1>Ola Mundo!</h1>  <p>ola django</p>")

def contato(request):
    return HttpResponse("<h1>Contato</h1>  <form>  <input type=text placeholder=email@email.com>  <input text=text placeholder=(21)99999-9999> <button>enviar</button> </form>")

#Aula 08
#Chamar arquivos HTML (Template)
def home(request):
    #Conceito de context (contexto)
    #Context - pega dados na view e passa para o template

    titulo = "Nossos melhores clientes "

    nosso_cliente = {
        'nome': "Thyago Assis de Almeida",
        'idade': 44,
        'nascimento': "15/021982"
    }

    nomes_clientes = ["Maria", "Joao", "Mateus", "Ana", "Marcos"]

    carros = [
        {'marca': "Chevrolet", 'modelo':'Onix LT', 'ano': '2020'},
        {'marca': "Fiat", 'modelo':'Uno', 'ano': '2010'},
        {'marca': "VW", 'modelo':'Gol', 'ano': '2022'},
    ]

    return render(request, "clientes/home.html", {'msg':titulo, 'lista_clientes':nosso_cliente, 'dados':nomes_clientes, 'meus_carros':carros})

def formulario(request):
    return render(request, "clientes/formulario.html" )