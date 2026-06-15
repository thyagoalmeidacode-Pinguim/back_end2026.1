from django.db import models

class Campus(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    #cria o atributo aluno e cria a relação
    
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)

    #Cria a relçao entre as tabelas
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

