from storage import salvar, carregar

tarefas = carregar()

if tarefas is None:
    tarefas = []


def adicionar_tarefa(titulo, prioridade, data):
    tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "concluida": False,
        "prioridade": prioridade,
        "data": data
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


# 🔥 NOVAS FUNÇÕES (FILTROS)

def filtrar_pendentes():
    return [t for t in tarefas if not t["concluida"]]


def filtrar_concluidas():
    return [t for t in tarefas if t["concluida"]]


def filtrar_por_prioridade(prioridade):
    return [t for t in tarefas if t.get("prioridade") == prioridade]