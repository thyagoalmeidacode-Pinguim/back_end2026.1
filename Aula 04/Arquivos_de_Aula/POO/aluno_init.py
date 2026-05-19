class Aluno:
    #Metodo contrutor(Tudo que tiver sera criado automaticammente quando a classe for usada)
    #O metodo __init__ é um metodo padrao
    def __init__(self, nome_aluno, idade_aluno): 

        #Atributos - vriaveis metidas
        self.nome = nome_aluno
        self.idade = idade_aluno

    def estudar(self):
        print(f"{self.nome}, Estudando python")

aluno_um = Aluno("Marcos", 25)

print(f"Nome: {aluno_um.nome}")
print(f"Idade: {aluno_um.idade}")
aluno_um.estudar()

print(20*"-")

aluno_dois = Aluno("Maria", 30)
print(f"Nome: {aluno_dois.nome}")
print(f"Idade: {aluno_dois.idade}")
aluno_dois.estudar()

print(20*"-")

nome = input("Informe o nome do primeiro aluno: ")
idade = int(input("Informe a idade: "))

aluno_tres = Aluno(nome,idade)
print(aluno_tres.nome)
print(aluno_tres.idade)
aluno_tres.estudar()