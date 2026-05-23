class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero_um = numero1
        self.numero_dois = numero2
    
    def soma(self):
        resultado = self.numero_um + self.numero_dois
        return resultado
    
    def subtrair(self):
        resultado = self.numero_um - self.numero_dois
        return resultado

    def multiplicar(self):
        resultado = self.numero_um * self.numero_dois
        return resultado

    def dividir(self):
        if self.numero_dois == 0:
            mensagem = "Impossivel divisão por zero"
        else: 
            resultado = self.numero_um / self.numero_dois
            return resultado
        

print("==== CALCULADORA MATEMATICA ====\n")
valor_um  = int(input("Informe o primeiro valor: "))
valor_dois = int(input("Informe o segundo valor: "))

calculadora_python = Calculadora(valor_um, valor_dois)

print(f"A soma é: {calculadora_python.soma()}")
print(f"A subtração é: {calculadora_python.subtrair()}")

print(f"A multiplicação é: {calculadora_python.multiplicar()}")
print(f"A divisão é: {calculadora_python.dividir()}")





    