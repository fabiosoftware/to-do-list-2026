# 📝 To-Do List PRO (Python)

## 🚀 Sobre o Projeto

Aplicação de linha de comando (CLI) desenvolvida em Python para gerenciamento de tarefas, com persistência em arquivo JSON e sistema de filtros inteligentes.

Este projeto foi construído com foco em boas práticas de programação, organização de código e simulação de um sistema real de produtividade.

---

## 🎯 Objetivo

Demonstrar habilidades em:

- Lógica de programação
- Estruturação de projetos Python
- Manipulação de dados (JSON)
- Versionamento com Git/GitHub
- Escrita de código limpo e funcional

---

## ⚙️ Funcionalidades

- ✅ Adicionar tarefas
- 📋 Listar tarefas
- ✔ Marcar tarefas como concluídas
- ❌ Remover tarefas
- 💾 Persistência de dados em JSON
- 🔍 Filtros inteligentes:
  - Tarefas pendentes
  - Tarefas concluídas
  - Filtro por prioridade

---

## 🧠 Tecnologias Utilizadas

- Python 3
- JSON (armazenamento de dados)
- Git & GitHub (versionamento)
- Programação procedural

---

## 🗂 Estrutura do Projeto

to-do-list-2026/
│
├── main.py        # Interface do usuário (menu CLI)
├── tarefas.py     # Regras de negócio
├── storage.py     # Leitura e escrita no JSON
├── tarefas.json   # Banco de dados simples
├── README.md
└── .gitignore

---

## ▶️ Como Executar

```bash
# Clonar repositório
git clone https://github.com/fabiosoftware/to-do-list-2026.git

# Acessar pasta
cd to-do-list-2026

# Executar o sistema
python main.py