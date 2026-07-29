#ENCAPSULAMENTO

# O QUE É? 
# IMAGINE CONTA BANCÁRIA E UM SALDO DE 1000000 DE REAIS
# POR ACASO É POSSÍVEL ALTERAR ESSE VALOR DE QUALQUER FORMA OU 
# EM QUALQUER PARTE DO SISTEMA?



class contabancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.__saldo = saldo # __ indica que o atributo é privado, ou seja, não pode ser acessado diretamente fora da classe

    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de '{valor}' realizado")

        else:
            print("Valor inválido")

    def sacar(self,valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print("Saque realizado")


    def mostrar_saldo(self):
        print(f"Saldo atual: {self.__saldo}")

conta1 = contabancaria("João", 113.6558)


conta1.__saldo = 10000
print()
conta1.mostrar_saldo()