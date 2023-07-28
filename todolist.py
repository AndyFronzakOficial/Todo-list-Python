
def exibir_menu():
    print("****** TO-DO LIST com Python ******")
    print("1. Adicionar tarefa")
    print("2. Exibir tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def exibir_tarefas(tarefas):
    print("****** TAREFAS ******")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")

def remover_tarefa(tarefas):
    exibir_tarefas(tarefas)
    numero_tarefa = int(input("Digite o número da tarefa que deseja remover: "))
    if 1 <= numero_tarefa <= len(tarefas):
        tarefas.pop(numero_tarefa - 1)
        print("Tarefa removida com sucesso!")
    else:
        print("Número de tarefa inválido.")

def main():
    tarefas = []
    
    while True:
        exibir_menu()
        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            adicionar_tarefa(tarefas)
        elif escolha == "2":
            exibir_tarefas(tarefas)
        elif escolha == "3":
            remover_tarefa(tarefas)
        elif escolha == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()

