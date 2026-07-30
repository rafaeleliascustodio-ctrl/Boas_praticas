from models.funcionario import Funcionario
from models.setor import setor

setor1 = setor(1,"TA")
funcionario1 = Funcionario(1,"Joaquim","Dev",5500.00,setor1)
funcionario1.aumentar_salario(-100)
funcionario1.apresentar()


# print("-"*20)
# setor1.nome = "Tech"
# setor1.apresentar
# setor1.nome = ""



    #restrição por encapsulamento != validação
'''
A distinção entre encapsular e validar é um pilar fundamental da Programação Orientada a Objetos,
pois o encapsulamento, por si só, apenas restringe os canais de acesso e modificação dos atributos.
A garantia de que um dado é íntegro e condizente com as regras do negócio permanece sob a responsabilidade 
do desenvolvedor, que deve programar os critérios de validação. É exatamente por essa razão que métodos 
modificadores como set_nome(), set_salario() e set_cargo() tornam-se indispensáveis: eles atuam como 
pontos centralizados de alteração dentro da classe, o que viabiliza a implementação e a futura manutenção 
de regras de validação sem a necessidade de reescrever ou impactar o restante do sistema.
'''