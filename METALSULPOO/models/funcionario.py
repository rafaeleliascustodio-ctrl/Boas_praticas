class Funcionario:
    def __init__(self, id, nome, cargo, salario, setor):
        self.__id = id
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario
        self.__setor = setor

    

    def apresentar(self):
        print("==== DADOS DO FUNCIONÁRIO ====")
        print("ID: ",self.__id)
        print("NOME: ",self.__nome)
        print("CARGO: ",self.__cargo)
        print("SALÁRIO: R$",self.__salario)
        print("SETOR: ", self.setor.nome)

    # def aumentar_salario(self, percentual):
    #     aumento = self.__salario * (percentual/100)
    #     self.__salario += aumento
    def trocar_cargo(self, novo_cargo):
        self.__cargo = novo_cargo   

    @property
    def setor(self):
        return self.__setor

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def cargo(self):
        return self.__cargo

    @property
    def salario(self):
        return self.__salario
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cargo.setter
    def cargo(self, cargo):
        if cargo == "":
            raise ValueError("O cargo não pode ser nulo.")
        self.__cargo = cargo

    @salario.setter
    def salario(self, valor):
        if valor < 0:
            raise ValueError(f"O Salário {valor} não pode ser negativo.")
        self.__salario = valor

    
    def aumentar_salario(self, valor):
        if valor <=0:
            raise ValueError(f"O aumento não deve ser menor que zero")
        self.__salario += valor

    