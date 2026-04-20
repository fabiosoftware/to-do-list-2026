import json
import os

ARQUIVO = "tarefas.json"

def salvar(tarefas):
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(tarefas, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print("Erro ao salvar tarefas:", e)
    import json
import os

ARQUIVO = "tarefas.json"


def carregar():
    if not os.path.exists(ARQUIVO):
        return []

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def salvar(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)    