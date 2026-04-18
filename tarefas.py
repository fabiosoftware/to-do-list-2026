from storage import salvar, carregar
tarefas = carregar()
if tarefas is None:
    tarefas = []


def adicionar_tarefa(titulo):
    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "concluida": False
    }
    tarefas.append(tarefa)
    salvar(tarefas)
    return tarefa


def listar_tarefas():
    return tarefas


def concluir_tarefa(id_tarefa):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["concluida"] = True
            salvar(tarefas)
            return tarefa
    return None


def remover_tarefa(id_tarefa):
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefas.remove(tarefa)
            salvar(tarefas)
            return True
    return False