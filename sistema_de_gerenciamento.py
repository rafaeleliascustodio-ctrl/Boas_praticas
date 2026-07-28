#Sistema de gerenciamento de tarefas (Aplicar a programação estruturada)

def exibir_menu():
    """exibir o menu principal do sistema"""
    print("\n"+"="*30)
    print("SISTEMA DE TAREFAS")
    print("="*30)
    print("1. listar tarefas")
    print("2. adicionar tarefas")
    print("3. concluir tarefas")
    print("4. remover tarefas")
    print("5. sair")
    print("="*30)

#Função para listar tarefas

def listar_tarefas(tarefas):
    """mostrar todas as tarefas cadastradas e seus status."""
    print("\n --- lista de tarefas ---")
    if not tarefas:
        print("Nenhuma tarefa.")
        return
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "concluida" if tarefa["concluida"] else "pendente"
        print(f"{indice}. [{status}] {tarefa['descrição']}")

def adicionar_tarefa(tarefas):
    """adicionar uma nova tarefa a lista"""
    descrição = input("\nDigite a descrição da tarefa: ")
    if descrição:
        nova_tarefa = {"descrição":descrição,"concluida":False}
        tarefas.append(nova_tarefa)
        print(f"Tarefa '{descrição}' adicionada com sucesso!")
    else:
        print("A descrição não pode estar vazia.")

def concluir_tarefa(tarefas):

    '''marcar uma tarefa como concluida'''
    listar_tarefas(tarefas)
    if not tarefas:
        return

    try:
        escolha = int(input("\nDigite o número da tarefa que deseja concluir: "))
        if 1 <= escolha <= len(tarefas):
            tarefas[escolha - 1]["concluida"] = True
            print(f"Tarefa '{tarefas[escolha - 1]['descrição']}' marcada como concluída!")
        else:
            print("Número da tarefa inválido.")
    except ValueError:
        print("Por favor, digite um número válido!!!!!!!!!!!!!!!!!!")

def remover_tarefa(tarefas):
    """remover uma tarefa da lista"""
    listar_tarefas(tarefas)
    if not tarefas:
        return
    
    try:
        escolha = int(input("\nDigite o número da tarefa que deseja remover: "))
        if 1 <= escolha <= len(tarefas):
            tarefa_removida = tarefas.pop(escolha - 1)
            print(f"Tarefa '{tarefa_removida['descrição']}' removida com sucesso!")

        else:
            print("Número da tarefa inválido.")
    except ValueError:
        print("Por favor, digite um número válido!!!!!!!!!!!!!!!!!!")

def main():
    """função principal do sistema de gerenciamento de tarefas"""
    tarefas = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
main()