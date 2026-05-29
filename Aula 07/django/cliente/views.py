from django.shortcuts import render #Ja vem por padrão

#Importar a classe (Ferramenta) HttpResponse
from django.http import HttpResponse #Vai responder a solicitação do navegador

#Cria a função que reposnde a solicitação do navegador
def ola_mundo(request):
    return HttpResponse("<h1>Ola Mundo!</h1>  <p>ola django</p>")

def contato(request):
    return HttpResponse("<h1>Contato</h1>  <form>  <input type=text placeholder=email@email.com>  <input text=text placeholder=(21)99999-9999> <button>enviar</button> </form>")