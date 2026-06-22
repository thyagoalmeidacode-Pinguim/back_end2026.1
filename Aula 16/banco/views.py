#get_object_or_404 permite pegar um objeto ou informa um erro de pagina not found (404)
#Redirect server para redirecionar para algum lugar

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages #Ferramenta para enviar mensaggens para o usuario
from django.db import IntegrityError
from decimal import Decimal


from .models import Cliente, Conta, Movimento
import random
 

#Função da pagina inicial
def index(request):
    return render(request, 'pages/home.html')

#Função para abrir conta
def abrir_conta(request):
    #O metodo post só existe se clicar no botão do formulario
    if request.method == "POST":
        nome_form = request.POST.get('nome') #Capturar o nome que foi digitado no formulario
        cpf_form = request.POST.get('cpf') #Captura o cpf digirado no fomulario

        #Retira pontos, traços e espaços (Padroniza o cpf)
        cpf_limpo = cpf_form.replace('.', '').replace('-', '').replace(' ','')

        if Cliente.objects.filter(cpf=cpf_limpo).exists():
            #Cria a mensagem de erro
            messages.error(request, 'CPF já cadastrado! Use outro CPF ou acesse uma conta exixtente.')
            return render(request, 'pages/abrir_conta.html')
        
        try:
            #Cadastrar o cliente no banco de dados
            #CRUD - Create,Read,Update,Delete
            cliente = Cliente.objects.create(nome=nome_form, cpf=cpf_limpo)

            #Gerar o numero da conta de forma aleatoria
            numero = (random.randint(10000, 99999))

            #Verifica se a conta existe
            while Conta.objects.filter(numero=numero).exists():
                 numero = str(random.randint(10000, 99999))
            
            #Cria a conta
            conta = Conta.objects.create(numero=numero, cliente=cliente)

            #Messagens dizendo que a conta foi criada
            messages.success(request, f'Conta criada com sucesso! Seu numero de conta é: {numero}')

            #redireciona para a conta apos a criação
            return redirect('conta', conta_id=conta.id)
        
        #Verifica erro de integridade
        except IntegrityError:  #Verifica a integridade do banco de dados (Caso exista um cliente com o mesmo CPF)
            messages.error(request, 'Erro ao criar conta. CPF já cadastrado')
            return render(request, 'pages/abrir_conta.html')
        
        except Exception as e: #Exibe erros aleatorios
            messages.error(request, f'Erro ao cria a conta: {str(e)}')
            return render(request, 'pages/abrir_conta.html')
    

    return render(request, 'pages/abrir_conta.html')

#Função da pagina da conta
def conta(request, conta_id):

    #Guarda a conta atarves do id
    conta = get_object_or_404(Conta, id=conta_id)

    return render(request, 'pages/conta.html', {'conta':conta})

#Função depositar
def depositar(request, conta_id):
    conta = get_object_or_404(Conta, id=conta_id)    

    if request.method == "POST":
        try:
            valor = Decimal(request.POST.get('valor_form')) #pega o valor do formulario
            if valor > 0: 
                #Metodo criado no model
                conta.depositar(valor)

                #Criar a movimetação
                Movimento.objects.create(conta=conta, tipo='deposito', valor=valor)
                messages.success(request, f"Depósito de R${valor:.2f} realizado!")

                #redireciona para a pagina conta
                return redirect('conta', conta_id=conta.id)
            else:
                messages.error(request, 'Valor invalido!')
        except:
            messages.error(request, 'Valor invalido!')


    return render(request, 'pages/depositar.html', {'conta': conta})