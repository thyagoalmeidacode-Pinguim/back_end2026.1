class ContaBancaria:

    def __init__(self):
        self.saldo = 0 

    def total_saldo(self):
        mensagem = f"O saldo atual é de R$ {self.saldo}"
        return mensagem

    def sobre_deposito(self):
        valor = int(input("Informe o valor a depositar: R$"))

        if valor > 0:
            self.saldo += valor
            print(f"Deposito de R${valor:.2f} foi feito")
        else:
            print("Não foi possivel fazer esse depósito")


cliente = ContaBancaria()
print(f"Antes do deposito {cliente.total_saldo()}")

cliente.sobre_deposito()
print(cliente.total_saldo())