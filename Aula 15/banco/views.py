from django.shortcuts import render
from django.contrib import messages #Ferramenta para enviar mensaggens para o usuario

from .models import Cliente, Conta
import random
 

#Função da pagina inicial
def index(request):
    return render(request, 'pages/home.html')

#Função para abrir conta
def abrir_conta(request):
    #O metodo post só existe se clicar no botão do formulario
    if request.method == "POST":
        nome_form = request.POST.get('nome') #Capturar o nome que foi digitado no foemulario
        cpf_form = request.POST.get('cpf') #Captura o cpf digirado no fomulario

        #Retira pontos, traços e espaços
        cpf_limpo = cpf_form.replace('.', '').replace('-', '').replace(' ','')

        if Cliente.objects.filter(cpf=cpf_limpo).exists():
            messages.error(request, 'CPF já cadastrado! Use outro CPF ou acesse uma conta exixtente.')
            return render(request, 'pages/abrir_conta.html')
        
        try 
            #Cadastrar o cliente no banco de dados
            #CRUD - Create,Read,Update,Delete
            cliente = Cliente.objects.create(nome=nome_form, cpf=cpf_limpo)

            #Gerar o numero da conta
            numero = str(random.randint(10000, 99999))

            #Verifica se a conta existe
            while Conta.objects.filter(numero=numero).exists():
                 numero = str(random.randint(10000, 99999))
            
            #Cria a conta
            conta = Conta.objects.create(numero=numero, cliente=cliente)

    return render(request, 'pages/abrir_conta.html')
  