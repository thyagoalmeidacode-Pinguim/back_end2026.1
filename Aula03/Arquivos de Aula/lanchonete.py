#Sistema Lanchonete

#Define as listas
lanches = []
precos = []
pedidos = []

#Função de mensagens
def mensagem(msg):
    print(msg)    

#Função cadastrar lanche
def cadastrar_lanche(lanche, preco):
    #append cadastro itens na lista
    lanches.append(lanche)
    precos.append(preco)
    return mensagem("Lanche cadastrado")

#Mostrar cardapio
def mostrar_cardapio():
    for i in range(len(lanches)):
        mensagem(f"{i} - {lanches[i]:.2f} - R${precos[i]:.2f}")

#Fazer pedido
def fazer_pedido(pedido):
    pedidos.append(precos[pedido])

def calcular_total():
    #A função sum soma os valores dentro de uma lista
    return sum(pedidos)

def menu():
    print("\n==== Lanchonete ====")
    print("1 - Cadastrar Lanche\n2 - Mostrar cardapio\n3 - Fazer Pedido\n4 - Mostrar total\n5 - Sair ")

#Aqui acontece a magica(Main)
def main():
    while True:
        menu()
        opcao = int(input("Escolha a opção pelo numero: "))
        if opcao == 1:
            lanche = input("Nome do lanche: ")
            preco = float(input("Informe o preço R$"))
            cadastrar_lanche(lanche, preco)
            mensagem("Lanche cadastroado com sucesso")
        elif opcao == 2:
            mensagem("\n==== Cardapio ====")
            mostrar_cardapio()
        elif opcao == 3:
            mensagem("\n==== Cardapio ====")
            mostrar_cardapio()
            escolha = int(input("Escolha o lanche pelo numero: "))
            fazer_pedido(escolha)
            mensagem("Pedido realizado!")
        elif opcao == 4:
            mensagem(f"O total é R${calcular_total():.2f}")        
        elif opcao == 5:
            mensagem("Saindo...")
            break
        else :
            mensagem("Opção invalida!")

main()