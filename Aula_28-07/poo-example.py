#classe em python
class carro:#é o modelo de todos os carros do meu sitema
    #método construtor
    def __init__ (self, marca, modelo, ano):
        #def init é o metodo construtor, será executado sempre na criação do objeto
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    #Método da classe
    def exibir_dados(self):
        print("=== Dados do Carro ===")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

#criando objetos
carro1 = carro("Volkswagen", "Santana Qantum", 1989)
carro2 = carro("Chevrolet", "Corsa", 2002)
#chamada do objeto e do método
carro1.exibir_dados()
print()
carro2.exibir_dados()

