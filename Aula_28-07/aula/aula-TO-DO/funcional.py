#Sistema de gerenciamento de tarefas(aplicar a programção estruturada)

def exibir_menu():
    """exibir o menu principal do sistema"""
    print("\n"+"="*30)
    print("SISTEMA DE TAREFAS")
    print("="*30)
    print("1. Listar tarefas")
    print("2. Adicionar tarefa")
    print("3. Concluir tarefa")
    print("4. Remover tarefa")
    print("5. Sair")
    print("="*30)


#função para listar tarefas
def listar_tarefas(tarefas):
    """Mostra todas as tarefas cadastradas e seus status"""
    print("\n --- LISTAGEM DE TAREFAS ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "concluida" if tarefa['concluida'] else 'pendente'
        print(f"{indice}. [{status}] {tarefa['descricao']}")

def adicionar_tarefas(tarefas):
    """Adicionar uma nova tarefa a lista"""

    descricao = input("\nDigite a descrição da tarefa: ")
    if descricao:
        nova_tarefa = {'descricao': descricao, 'concluida': False}
        tarefas.append(nova_tarefa)
        print(f"Tarefa '{descricao}' adicionada com sucesso!")
    else:
        print("A descrição da tarefa não pode ser vazia.")

def concluir_tarefa(tarefas):
    """Marca uma tarefa como concluída"""
    listar_tarefas(tarefas)
    if not tarefas:
        return

    try:
        escolha = int(input("\nDigite o número da tarefa a ser concluída: "))
        if 1 <= escolha <= len(tarefas):
            tarefas[escolha - 1]['concluida'] = True
            print(f"Tarefa '{tarefas[escolha - 1]['descricao']}' concluída com sucesso!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def remover_tarefa(tarefas):
    """Remove uma tarefa da lista"""
    listar_tarefas(tarefas)
    if not tarefas:
        return

    try:
        escolha = int(input("\nDigite o número da tarefa a ser removida: "))
        if 1 <= escolha <= len(tarefas):
            tarefa_removida = tarefas.pop(escolha - 1)
            print(f"Tarefa '{tarefa_removida['descricao']}' removida com sucesso!")
        else:
            print("Número de tarefa inválido.")


    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

def main():
    """Função principal do sistema de gerenciamento de tarefas"""
    tarefas = []
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            listar_tarefas(tarefas)
        elif escolha == '2':
            adicionar_tarefas(tarefas)
        elif escolha == '3':
            concluir_tarefa(tarefas)
        elif escolha == '4':
            remover_tarefa(tarefas)
        elif escolha == '5':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

#ponto de partida do programa
if __name__ == "__main__":
    main()