class ContaBancaria:
    def __init__(self):
        #Inicia o saldo
        self.saldo = 0

    def mostra_saldo(self):
        print(f"Você armazenou R${self.saldo}")

    def depositando(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Você depositou R${valor}")
        else:
            print("Você deve depositar um valor positivo")

    def saldo_final(self):
        print(f"Seu saldo atual é de R${self.saldo}")

valores = ContaBancaria()
valores.mostra_saldo()
valores.depositando(1000)
valores.saldo_final()
