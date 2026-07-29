#Classe em python
class carro: #Modelo de todos os carros do meu sistema
    #Método construtor
    def __init__(self, marca, modelo, ano):
        #def init é o método construtor da classe, ele é chamado automaticamente quando um objeto é criado
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


    #metodo da classe
    def exibir_informacoes(self):
        print("\n--- Informações do carro ---")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

#criando objetos
carro1 = carro("Toyota", "Corolla", 2020)
carro2 = carro("Honda", "Civic", 2019)

#exibindo informações dos carros. Objetos e métodos
carro1.exibir_informacoes()
carro2.exibir_informacoes()
