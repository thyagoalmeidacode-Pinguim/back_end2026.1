#get_object_or_404 permite pegar um objeto ou informa um erro de pagina not found (404)
#Redirect server para redirecionar para algum lugar

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages #Ferramenta para enviar mensaggens para o usuario
from django.db import IntegrityError
from decimal import Decimal

from .models import Cliente, Conta, Movimento
import random 

from django.http import HttpResponse

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
            
            request.session['conta_numero'] = numero
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

    #Valida se o usuraio esta autenticado
    if 'conta_numero' not in request.session or request.session['conta_numero'] != conta.numero:
        messages.warning(request, 'Por favor, acesse sua conta primeiro')
        return redirect('acessar_conta') 

    #Pegar as movimentações(Seleciona os movimento, ordena pela data, exibe somente os 5 ultimos)
    movimentos = conta.movimento_set.all().order_by('-data')[:5]

    return render(request, 'pages/conta.html', {'conta':conta, 'movimentos': movimentos})

#Função depositar
def depositar(request, conta_id):
    conta = get_object_or_404(Conta, id=conta_id)

    #Valida se o usuraio esta autenticado
    if 'conta_numero' not in request.session or request.session['conta_numero'] != conta.numero:
        messages.warning(request, 'Por favor, acesse sua conta primeiro')
        return redirect('acessar_conta')

    #Verifica se a conta existe, caso nao da o error 404 (Pagina não encontrada)
   

    if request.method == "POST":
        try:
            valor = Decimal(request.POST.get('valor_form')) #pega o valor do formulario
            if valor > 0: 
                #Metodo criado no model
                conta.depositar(valor)
                #Registra o deposito
                Movimento.objects.create(conta=conta, tipo='deposito', valor=valor)           
                messages.success(request, f"Depósito de R${valor:.2f} realizado!")
                #redireciona para a pagina conta
                return redirect('conta', conta_id=conta.id)
            else:
                messages.error(request, 'Valor invalido!')
        except:
            messages.error(request, 'Valor invalido!')


    return render(request, 'pages/depositar.html', {'conta': conta})

def saque(request, conta_id):
    conta = get_object_or_404(Conta, id=conta_id)

    #Valida se o usuraio esta autenticado
    if 'conta_numero' not in request.session or request.session['conta_numero'] != conta.numero:
        messages.warning(request, 'Por favor, acesse sua conta primeiro')
        return redirect('acessar_conta')

    #Verificar se o botão do formulario foi pressionado
    if request.method == "POST":
        try: 
            valor = Decimal(request.POST.get('valor_form'))

            #if valor > 0 and conta.saldo >= valor:

            if valor > 0 and conta.sacar(valor):
                #Registra o saque
                Movimento.objects.create(conta=conta, tipo='saque', valor=valor)
                messages.success(request, f"Saque de R$ {valor:.2f} reaizado!")
                return redirect('conta', conta_id=conta.id)
            else:
                messages.error(request, 'Saldo insuficiente ou Valor invalido!')
        except:
            messages.error(request, 'Saldo insuficiente ou Valor invalido!')
    
    return render(request, 'pages/sacar.html', {'conta':conta})
    
def acessar_conta(request):
    #Cptura os do forumulario
    if request.method == "POST":
        numero_conta = request.POST.get('numero_form')
        cpf_cliente = request.POST.get('cpf_form')

        #Retira pontos, traços e espaços
        cpf_limpo = cpf_cliente.replace('.', '').replace('-', '').replace(' ','')

        try:
            conta = Conta.objects.get(numero=numero_conta) #Captura no banco dados a conta informada
            usuario = conta.cliente #Pega no banco de dados todos os dados do cliente

            if usuario.cpf != cpf_limpo:
                messages.error(request, 'CPF não correposnde ao número da conta')
                #Retorna para a tela de login (acessar conta)
                return render(request, 'pages/acessar_conta.html')
            
            #Cria a Sessão / Para bloquer acesso as paginas sem autenticação
            request.session['conta_numero'] = numero_conta
            messages.success(request, f"Bem vindo de volta, {conta.cliente.nome}")
            
            #Direciona para a conta
            return redirect('conta', conta_id=conta.id)
        
        except Conta.DoesNotExist:
            messages.error(request, 'Conta não encontrada! Verifique o numero.')
    
    return render(request, 'pages/acessar_conta.html')
 
def logout(request):
    #Encerra toda sessao que exista
    if 'conta_numero' in request.session:
        del request.session['conta_numero']
        messages.info(request, 'Você saiu da conta!')
    return redirect("inicio")


























    
# Cria o cookie Cokies
def criar_cookie(request):
    response = HttpResponse('Cokie Criado')
    #set_cookie => Cria o cookie
    response.set_cookie('cor', 'Amarelo')
    return response

#Exibe o cookie 
def ler_cookie(request):
    minha_cor = request.COOKIES.get('cor')
    return HttpResponse(f"A cor favorita é: {minha_cor}")


#Criação de sessao
def login(request):
    if request.method == 'POST':
        usuario_form = request.POST.get('usuario')
        senha_form = request.POST.get('senha')

        if usuario_form == 'admin' and senha_form == '123':
            #cria a sesçao (session)
            request.session['usuario'] = usuario_form
            request.session['senha'] = senha_form

            messages.success(request, "Login realizado com sucesso!")
            return redirect("home")        
        else:
            messages.error(request, "Usuário ou senha invalidos")
    
    return render(request, 'pages/login.html')

#Função home

def home(request):
    #Verifico se a sessão foi criada - Permite acesso se fizer login
    if "usuario" not in request.session:
        return redirect("login")
    
    meu_usuario = request.session["usuario"]
    return render(request, "pages/inicio.html", {'usuario': meu_usuario})

#Função logout


    
    
    
    
    """ 
        Desafio: Desenvolver o modulo de saque 
            - Criar a função de saque na views
            - Ciar o template (Formulario)
            - Configurar a URL
            - Configurar o botao de saque da conta      
    """