from tarefas import (
    adicionar_tarefa,
    listar_tarefas,
    concluir_tarefa,
    remover_tarefa,
    filtrar_pendentes,
    filtrar_concluidas,
    filtrar_por_prioridade
)


def menu():
    while True:
        print("\n===== TO-DO LIST PRO =====")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Filtrar tarefas")
        print("6 - Sair")
        print("==========================")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            titulo = input("Digite a tarefa: ")
            prioridade = input("Prioridade (baixa, media, alta): ")
            data = input("Data de vencimento (dd/mm/aaaa): ")

            adicionar_tarefa(titulo, prioridade, data)
            print("✔ Tarefa adicionada!")

        elif opcao == "2":
            tarefas = listar_tarefas()

            if not tarefas:
                print("\n📭 Nenhuma tarefa cadastrada.\n")
            else:
                print("\n===== SUAS TAREFAS =====")
                for t in tarefas:
                    status = "✔ Concluída" if t["concluida"] else "✘ Pendente"
                    print(f"ID: {t['id']} | {t['titulo']} | {t['prioridade']} | {t['data']} | {status}")
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
            print("\n1 - Pendentes")
            print("2 - Concluídas")
            print("3 - Por prioridade")

            escolha = input("Escolha o filtro: ")

            if escolha == "1":
                resultado = filtrar_pendentes()

            elif escolha == "2":
                resultado = filtrar_concluidas()

            elif escolha == "3":
                prioridade = input("Digite (baixa, media, alta): ")
                resultado = filtrar_por_prioridade(prioridade)

            else:
                print("⚠ Opção inválida!")
                continue

            if not resultado:
                print("\n📭 Nenhuma tarefa encontrada.\n")
            else:
                print("\n===== RESULTADO =====")
                for t in resultado:
                    status = "✔" if t["concluida"] else "✘"
                    print(f"{t['id']} | {t['titulo']} | {t['prioridade']} | {t['data']} | {status}")
                print("=====================\n")

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("⚠ Opção inválida! Tente novamente.")


menu()