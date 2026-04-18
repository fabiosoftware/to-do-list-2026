from tarefas import adicionar_tarefa, listar_tarefas, concluir_tarefa, remover_tarefa


def menu():
    while True:
        print("\n===== TO-DO LIST =====")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")
        print("======================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titulo = input("Digite a tarefa: ")
            adicionar_tarefa(titulo)
            print("✔ Tarefa adicionada!")

        elif opcao == "2":
            tarefas = listar_tarefas()

            if not tarefas:
                print("\n📭 Nenhuma tarefa cadastrada.\n")
            else:
                print("\n===== SUAS TAREFAS =====")
                for t in tarefas:
                    status = "✔ Concluída" if t["concluida"] else "✘ Pendente"
                    print(f"ID: {t['id']} | {t['titulo']} | {status}")
                print("=========================\n")

        elif opcao == "3":
            try:
                id_tarefa = int(input("ID da tarefa: "))
                concluir_tarefa(id_tarefa)
                print("✔ Tarefa concluída!")
            except ValueError:
                print("⚠ Digite um número válido!")

        elif opcao == "4":
            try:
                id_tarefa = int(input("ID da tarefa: "))
                remover_tarefa(id_tarefa)
                print("✔ Tarefa removida!")
            except ValueError:
                print("⚠ Digite um número válido!")

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("⚠ Opção inválida! Tente novamente.")


menu()