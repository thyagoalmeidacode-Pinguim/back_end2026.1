class Animal:

    def __init__(self,nome_animal, idade_animal, raca_animal, tipo_animal):
        self.nome = nome_animal
        self.idade = idade_animal
        self.raca = raca_animal
        self.tipo = tipo_animal
    
    def desc_animal(self):
        print(f'O animal {self.nome},\na idade é {self.idade},\nraça:{self.raca},\nTipo: {self.tipo}')

#---------------------------------

class Petshop:
    def __init__(self):
        self.cadastro = []

    def cadastrar_animal(self):
        print("\n--- Cadastro de Animal ---")
        nome = input("Nome do animal: ")
        idade = input("Idade do animal: ")
        raca = input("Raça do animal: ")
        tipo = input("Tipo do animal (Ex: Cão, Gato): ")
        
        meu_animal = Animal(nome, idade, raca, tipo)
    
    # Adiciona o animal na lista do Petshop
        self.cadastro.append(meu_animal)
        print(f"¡{nome} cadastrado com sucesso!\n")

    def mostrar_animais(self):
        for meu_animal in self.cadastro:
            meu_animal.desc_animal()
            print("-" * 20)

    def main (self):
        while True:
            print("Bem-vindo ao Petshop!\n")
            print("1 - Cadastrar animal")
            print("2 - Mostrar animais cadastrados")
            print("3 - Sair\n")
            opcao = int(input("Digite a opção desejada: "))
            
            if opcao == 1:
                self.cadastrar_animal()
            elif opcao == 2:
                self.mostrar_animais()
            elif opcao == 3:
                print("Obrigado por usar o Petshop! Até mais!")
                break
            else:
                print("Opção inválida. Por favor, tente novamente.\n")

#Execução do progrma
loja = Petshop()
loja.main()