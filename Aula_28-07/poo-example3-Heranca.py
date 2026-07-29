#HERANÇA 
#sUPONHA QUE EXISTAM VÁRIOS VEÍCULOS, TODOS POSSUEM RODAS, ACELERAR E FREIAR
#LOGO, NÃO FAZ SENTIDO REPETIR CÓDIGO, PODEMOS CRIAR UMA CLASSE GERAL, E DEPOIS FAMOS OUTRAS PARA HERDAREM DELA.

#PAI
class veiculo:
    def __init__(self, rodas):
        self.rodas = rodas

    def acelerar(self):
        print("Acelerando...")

    def freiar(self):
        print("Freando...")


#FILHO
#O carro herda tudo da classe veiculo
class carro(veiculo): # é obrigatorio a declaração class filha(nome da classe pai)
    def __init__(self, marca, modelo):
        super().__init__(4) #Executa o construtor da classe pai
        #atributo da classe pai
        self.marca = marca
        self.modelo = modelo
        print(f"Criando um carro {self.marca} com {self.rodas} rodas")

carro1 = carro("Toyota", "Corolla")
carro1.acelerar()