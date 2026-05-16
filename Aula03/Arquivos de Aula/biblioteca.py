#Bibloiteca

biblioteca = []
emprestimos = []

def mensagem(msg):
    print(msg)

def cadastro_livros():
    nome_livro = input("Nome do livro: ")
    autor_livro = input("Autor do livro: ")

    #Dicionario do python
    livro = {
        'nome': nome_livro,
        'autor': autor_livro,
        'quantidade': 12
    }

    biblioteca.append(livro)
    mensagem("Livro cadastrado!")

def mostrar_livros():
    mensagem("\n==== LIVROS ====")
    for i in range(len(biblioteca)):
        mensagem(f"{i} - {biblioteca[i]}")


def emprestimo_livros():
    #Chama a função Mostrar livros
    mostrar_livros()
    escolha = int(input("Escolha o livro pelo número: "))
    emprestimos.append(biblioteca[escolha])
    mensagem("Livro emprestado com sucesso!")

def total_emprestimo():
    return len(emprestimos)

def menu():
    print("\n==== BIBLIOTECA DO PYTHON ====")
    print("1 - Cadastrar Livros")
    print("2 - Mostrar Livros")
    print("3 - Emprestar Livros")
    print("4 - Total de emprestimos")
    print("5 - Sair")

def main():
    while True:
        menu()
        opcao = int(input("O que deseja fazer?: "))
        if opcao == 1: 
            cadastro_livros()
        elif opcao == 2:
            mostrar_livros()
        elif opcao == 3:
            emprestimo_livros()
        elif opcao == 4:
            mensagem(f"Total de emprestimos: {total_emprestimo()}")
        elif opcao == 5:
            mensagem("Saindo...")
            break
        else:
            mensagem("Opção invalida!")

main()

