from django.db import models

#Model Cliente
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.nome

#Model Conta  
class Conta(models.Model):
    numero = models.CharField(max_length=10, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) #Relação com cliente
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Conta {self.numero} - {self.cliente.nome}"
    
    def depositar(self, valor):
        self.saldo += valor
        self.save() #Grava no banco de dados

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.save()
            return True
        
        return False
    

#Model movimentação
class Movimento(models.Model):
    TIPO_CHOICES = [
            ('deposito', 'Depósito'),
            ('saque', 'Saque')
        ]

    conta = models.ForeignKey(Conta, on_delete=models.CASCADE) #relcionamento com a conta
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True) #Registra a data e a hora de forma autmoatica

    def __str__(self):
        return f"{self.tipo} - R$ {self.valor}"

