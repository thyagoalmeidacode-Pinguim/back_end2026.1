
#A palavra class é a paçavra reservada para criar um classe
#A classe é um molde do objeto
#Iniciar o nome da classe com letra maíscula
class Carro:
    
    #Metodo = Função
    #Self representa o proprio metodo e seus elementos
    def buzinar(self, nome):
        self.nome
        print("Bibibi")

    def andar(self):
        print("Em movimento")


#Cria o objeto utilizando a classe (Molde)
carro_um = Carro() #Instanciar a classe
carro_um.buzinar()
carro_um.andar()