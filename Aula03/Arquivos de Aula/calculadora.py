""" Passagenm de parametro é quando envoamos informações para a função, de forma que ela possar executar sua tarefa """

#Criamos a função       
def calculo(valor_um,operador,valor_dois):
    if operador == "+":
        resultado = valor_um + valor_dois
        return resultado
    elif operador == "-":
        resultado = valor_um - valor_dois
        return resultado
    elif operador == "*":
        resultado = valor_um * valor_dois
        return resultado
    elif operador == "/":

        #Evita o erro da divisão por zero
        if valor_dois == 0:
            #Boa pratica colocar a mensagem em uma varivel para depois retornar
            mensagem = "Não é possivel divisão por zero!"
            return mensagem
        else:
            resultado = valor_um / valor_dois
            return resultado

#Programação:
#para a progamação utilize a função padrão main

#Utilizar a função main (Principal)

def main():
    print("Bem vindo(a) a calculadora do Python\n")
    print(30*"=")

    numero_um = int(input("Informe o primeiro valor: "))
    op = input("Informe a operação [+] [-] [*] [/]: ")
    numero_dois = int(input("Informe o segundo valor: "))

    print(f"O resultado é: {calculo(numero_um,op,numero_dois)}")

main()

