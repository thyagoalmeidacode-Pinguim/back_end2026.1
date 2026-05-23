class Animal:
    def __init__(self,nome_animal,idade_animal,tipo_animal):
        self.nome = nome_animal
        self.idade = idade_animal
        self.tipo = tipo_animal
        
    def mostrar_dados(self):
        print(f'O animal {self.nome},\na idade é {self.idade},\nTipo: {self.tipo}')


#-------------------------------------------------------------------------
class Petshop:
    def __init__(self):
        self.animais = [] #Lista que guarda os animais

    def cadastar_animal(self):
        nameani = input('Digite o nome do animal: ')
        ageani = input('Digite a idade do animal: ')
        typeani = input('Qual o tipo do animal ex: gato, cachorro: ')       

        #Instancia a clase Animal dentro da classe PetShop
        #Herança é uma ligação (petshop ao animal)
        meu_animal = Animal(nameani,ageani,typeani) #Objeto - Caacterisiticas

        self.animais.append(meu_animal)#Cadastra o objeto na lista
        print("Animal Cadastrado!\n")
    
    def mostrar_animais(self):
        print('\n==== ANIMAIS CADASTRADOS ====')        
        for meu_animal in self.animais:
            meu_animal.mostrar_dados()

    def main(self): 
        while True:
            try:
                opcao = int(input("\nEscolha um opção:\n[1 - cadastrar]\n[2 - Mostrar]\n[3 - Sair]\n ->"))
                if opcao == 1:             
                    self.cadastar_animal()
                elif opcao == 2:
                    self.mostrar_animais()
                elif opcao == 3:
                    print("\nSaindo. Até logo!")
                    break
            except ValueError:
                print(46*("-"))
                print("Operação inválida! Por favor, tente novamente.")


print(46*("-"))

anim = Petshop()
anim.main()