filmes = []
precos_ingresso = []


#FUNÇÕES 

#Função de mensagem
def mensagem(msg):
    return msg

#Função para cdastrar os filmes
def cadastro_filme():
    nome_filme = input("Nome do Filme: ")
    genero_filme = input("Genero: ")
    autor_filme = input("Autor: ")
    preco_sessao = input("Valor da sessão: ")

    #Dicionario (Objeto)
    filme = {
        'nome': nome_filme,
        'genero': genero_filme,
        'autor': autor_filme
    }

    filmes.append(filme) #Cadastra o filme na lista Filmes
    precos_ingresso.append(preco_sessao) #Cadastra o valor do ingresso na lista precos_ingresso
    return mensagem("Filme cadastrado com sucesso!")



print(cadastro_filme())

print(filmes)