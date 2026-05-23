class Animal:
    def __init__(self,nome_animal,idade_animal,tipo_animal):
        self.nome = nome_animal
        self.idade = idade_animal
        self.tipo = tipo_animal
        
    def mostrar_dados(self):
        print(f'O animal {self.nome},\na idade é {self.idade},\nTipo: {self.tipo}')