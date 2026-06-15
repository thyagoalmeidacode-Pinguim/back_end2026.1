from django.shortcuts import render

#Função da pagina inicial
def index(request):
    return render(request, 'pages/home.html')

#Função para abrir conta
def abrir_conta(request):
    return render(request, 'pages/abrir_conta.html')