""" Funçao com passagem de parametros """
def ola(nome):
    print(f"Ola {nome}!")

nome_usuario = input("Inisra seu nome: ")
nome_usuario_dois = input("Inisra seu nome: ")

ola(nome_usuario)
ola(nome_usuario_dois)