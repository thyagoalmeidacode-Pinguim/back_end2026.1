class Animal:
    def __init__(self,nome_animal, idade_animal, raca_animal, tipo_animal, som_animal):
        self.nome = nome_animal
        self.idade = idade_animal
        self.raca = raca_animal
        self.tipo = tipo_animal
        self.som = som_animal

    def desc_animal(self):
        print(f'O animal {self.nome},\na idade é {self.idade},\nraça:{self.raca}')

    def emitir_som(self):
        mensagem = f'O animal {self.nome}, faz {self.som}'
        return mensagem

class PetShop:
    def __init__(self):
        self.cadastro = [] #lista

    def cadastrar_animal(self):

        meu_animal = Animal("Amora", "2 meses", etc...)
        meu_animal.desc_animal()


    def mostre_animais(self):

    
    def main(self):



cachorro = Animal('Amora','3 meses','bulldog','cachorro','Au Au')
cachorro.desc_animal()
print(cachorro.emitir_som())

print(10*"=")

gato = Animal("Fifi", "2 anos", "vira lata", "gato", "Miau Miau")
gato.desc_animal()
print(gato.emitir_som())
