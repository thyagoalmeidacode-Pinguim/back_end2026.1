# "SISTEMA DE CINEMA"
filmes_cartaz = []
precos_ingresso = []
vendas = []

#FUNÇÕES 

#Função de mensagem
def mensagem(msg):
    print(msg)

#Função para cdastrar os filmes
def cadastro_filme():
    nome_filme = input("Nome do Filme: ")
    genero_filme = input("Genero: ")
    autor_filme = input("Autor: ")
    preco_sessao = int(input("Valor da sessão: "))

    #Dicionario (Objeto)
    filme = {
        'nome': nome_filme,
        'genero': genero_filme,
        'autor': autor_filme
    }

    filmes_cartaz.append(nome_filme) #Cadastra o filme na lista Filmes
    precos_ingresso.append(preco_sessao) #Cadastra o valor do ingresso na lista precos_ingresso
    return mensagem("Filme cadastrado com sucesso!")

#Mostrar Filme
def mostrar_filme():
    mensagem("\n ===== FILMES =====")
    for i in range(len(filmes_cartaz)):
        mensagem(f" {i} - {filmes_cartaz[i]} - R${precos_ingresso[i]}")

#Função vender ingresso
def vender_ingressos():
    mostrar_filme()
    escolha = int(input("Escolha o numero do Filme: "))
    vendas.append(precos_ingresso[escolha])
    mensagem("Ingresso vendido com sucesso!")

#Função calcula total de vendas
def calcula_total():
    return sum(vendas)

#Fnção calcula a quantidade de vendas
def total_ingressos():
    return len(vendas)

def menu():
    mensagem("\n ==== CINEMA =====")
    mensagem("1 - Cadastrar Filme")
    mensagem("2 - Mostrar Filme")
    mensagem("3 - Comprar Ingresso")
    mensagem("4 - Mostrar arrecadação")
    mensagem("5 - Total de ingressos")
    mensagem("6 - Sair")

#Funçõa main

def main():
    #Exibir o menu
    while True: 
        menu()

        opcao = int(input("Esscolha uma opção [1] [2] [3] [4] [5] [6]: "))

        if opcao == 1: 
            cadastro_filme()
        elif opcao == 2: 
            mostrar_filme()
        elif opcao == 3:          
            vender_ingressos()
        elif opcao == 4:
            mensagem(f" Arrecadação: R${calcula_total()}")
        elif opcao == 5: 
            mensagem(f"Ingressos vendidos: {total_ingressos()}")
        elif opcao == 6:
            mensagem("Saindo...")
            break
        else:
            mensagem("Opção invalida!")

main()