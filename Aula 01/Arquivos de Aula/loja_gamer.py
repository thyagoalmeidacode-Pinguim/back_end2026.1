""" Estudo de Caso: Loja de Games """

#Declarar as listas
jogos = ["Minecraft", "GTA V", "FIFA", "PAC MAN"]
precos = [80, 120, 90, 50]

total = 0

#Exibe menu para escolha
for i in range(len(jogos)):
    print(i, "-", jogos[i],"- R$", precos[i] )

#Usuario seleciona 
for i in jogos:
    escolha = int(input("Escolha o jogo: [0] [1] [2] [3]: "))
    total += precos[escolha]

    seguir = input("Deseja escolher outro jogo? [s] [n]").lower()

    if seguir in ["s", "sim"]:
        continue
    else:
        break

if total > 200:
    desconto = total * 0.10
    total -= desconto
    print("Desconto aplicado!")

print(f"Total Final: R${total:.2f}")