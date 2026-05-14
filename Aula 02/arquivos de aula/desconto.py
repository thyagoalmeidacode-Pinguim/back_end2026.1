#Cria uma função que de 10% 
def desconto_10(valor_compra):
    #Calcula qunto é 10% do valor da compra
    desconto = valor_compra * 0.10
    return valor_compra - desconto

valor = int(input("Informe o valaor da compra: "))
print("Aplicando cupom de 10%. Aguarde.. ")
valor_desconto = desconto_10(valor)

print(f"Desconto aplicado! Valor a pagar R${valor_desconto:.2f}")