#ENCAPSULAMENTO
#IMAGINE UMA CONTA BANCÁRIA E UM SALDO DE UM MILHÃO DE REAIS
#POR ACASO É POSSÍVEL ALTERAR ESSE VALOR DE QUALQUER FORMA?
#OU EM QUALQUER PARTE DO SISTEMA?

class contabancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo
        #__ indica que o atributo é private
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito realizado!\n")
        else:
            print(f"Valor inválido.\n")

    def sacarvalor(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque realizado!\n")
        else:
            print(f"Saldo insuficiente.\n")

    def mostrar_saldo(self):
        print(f"\n{self.__titular} Seu saldo disponível é: R$ {self.__saldo:.2f}\n")

#criando objetos
conta1 = contabancaria("João Valentim", 1000000)
conta1.mostrar_saldo()
conta1.depositar(66676767)
conta1.mostrar_saldo()
conta1.sacarvalor(67000000)
conta1.mostrar_saldo()

conta1.__saldo = 1080
print("_")
conta1.mostrar_saldo()

x = 20
x = 1000