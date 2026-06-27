from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from decimal import Decimal
from django.db import IntegrityError
from .models import Cliente, Conta, Movimento
import random

def index(request):
    return render(request, 'pages/home.html')

def abrir_conta(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        
        # Limpa o CPF (remove pontos e traços)
        cpf_limpo = cpf.replace('.', '').replace('-', '').replace(' ', '')
        
        # Verifica se CPF já existe (mais seguro)
        if Cliente.objects.filter(cpf=cpf_limpo).exists():
            messages.error(request, 'CPF já cadastrado! Use outro CPF ou acesse sua conta existente.')
            return render(request, 'pages/abrir_conta.html')
        
        try:
            # Cria o cliente
            cliente = Cliente.objects.create(nome=nome, cpf=cpf_limpo)
            
            # Gera número da conta aleatório
            numero = str(random.randint(10000, 99999))
            
            # Garante que o número é único
            while Conta.objects.filter(numero=numero).exists():
                numero = str(random.randint(10000, 99999))
            
            # Cria a conta
            conta = Conta.objects.create(numero=numero, cliente=cliente)
            
            messages.success(request, f'Conta criada com sucesso! Seu número de conta é: {numero}')
            # Salva o número da conta na sessão
            #request.session['conta_numero'] = numero
            return redirect('conta', conta_id=conta.id)
            
        except IntegrityError:
            messages.error(request, 'Erro ao criar conta. CPF já existe!')
            return render(request, 'banco/abrir_conta.html')
        except Exception as e:
            messages.error(request, f'Erro ao criar conta: {str(e)}')
            return render(request, 'pages/abrir_conta.html')
    
    return render(request, 'pages/abrir_conta.html')



def conta(request, conta_id):
    # Verifica se o usuário tem acesso a esta conta
    conta = get_object_or_404(Conta, id=conta_id)
    
    # Opcional: verificar sessão para segurança básica
    """ if 'conta_numero' not in request.session or request.session['conta_numero'] != conta.numero:
        messages.warning(request, 'Por favor, acesse sua conta primeiro.')
        return redirect('acessar_conta') """
    
    movimentos = conta.movimento_set.all().order_by('-data')[:5]
    return render(request, 'banco/conta.html', {'conta': conta, 'movimentos': movimentos})

def depositar(request, conta_id):
    #Busca a conta, caso nao exista retorna error 404 objrto nao encontrado
    conta = get_object_or_404(Conta, id=conta_id)
    
    # Verificar sessão
    """ if 'conta_numero' not in request.session or request.session['conta_numero'] != conta.numero:
        messages.warning(request, 'Por favor, acesse sua conta primeiro.')
        return redirect('acessar_conta')
     """
    if request.method == 'POST':
        try:
            valor = Decimal(request.POST.get('valor', '0'))
            
            if valor > 0:
                conta.depositar(valor)
                Movimento.objects.create(
                    conta=conta, 
                    tipo='deposito', 
                    valor=valor
                )
                messages.success(request, f'Depósito de R$ {valor:.2f} realizado!')
                return redirect('conta', conta_id=conta.id)
            else:
                messages.error(request, 'Valor inválido!')
        except:
            messages.error(request, 'Valor inválido!')
    
    return render(request, 'banco/depositar.html', {'conta': conta})

def sacar(request, conta_id):
    conta = get_object_or_404(Conta, id=conta_id)
    
    # Verificar sessão
    """ if 'conta_numero' not in request.session or request.session['conta_numero'] != conta.numero:
        messages.warning(request, 'Por favor, acesse sua conta primeiro.')
        return redirect('acessar_conta') """
    
    if request.method == 'POST':
        try:
            valor = Decimal(request.POST.get('valor', '0'))
            
            if valor > 0 and conta.sacar(valor):
                Movimento.objects.create(
                    conta=conta, 
                    tipo='saque', 
                    valor=valor
                )
                messages.success(request, f'Saque de R$ {valor:.2f} realizado!')
                return redirect('conta', conta_id=conta.id)
            else:
                messages.error(request, 'Saldo insuficiente ou valor inválido!')
        except:
            messages.error(request, 'Valor inválido!')
    
    return render(request, 'banco/sacar.html', {'conta': conta})

def sair(request):
    """Sair da conta"""
    if 'conta_numero' in request.session:
        del request.session['conta_numero']
        messages.info(request, 'Você saiu da sua conta.')
    return redirect('index')