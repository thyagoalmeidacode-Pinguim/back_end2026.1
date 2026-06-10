from django.db import models

# Aqui iremos criar nossos modelos.

class Cliente(models.Model):
    nome = models.CharField(max_length=100) #Definir campo, tipo e comprimento
    cpf = models.CharField(max_length=14, unique=True) #unique=True - Determina unico cpf por pessoa
    telefone = models.CharField(max_length=20)

    #Metodo para exibir os clientes por nome
    def __str__(self):
        return self.nome

class Conta(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2) #decimal_places Determina quantidade de casas

    #Relação com a tabela clientes
    cliente  = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero