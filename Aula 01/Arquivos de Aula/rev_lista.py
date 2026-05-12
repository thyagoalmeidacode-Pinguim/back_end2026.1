""" Crie uma lista que guarde as ramas do jogo """

""" Lista(Array) """
inventario = ["Espada", "Poção", "Escudo"]

print("Inventario 01")
for i in inventario:
    print(i)

print("")

inventario.append("Lança") #Adiciona mais itens

print("Inventario 02")
for i in inventario:
    print(i)

""" Tupla é imutavel """

valor_ataque = (10, 20)

valor_ataque.append(30)