# bd.py é o módulo que contém as funções para manipular o banco de dados

'''
Modelo do bd será:
KANBANS/ -> Arquivos JSON
    Kanban1.json
    {
        "Coluna1": {
            "Tarefa1": "Pessoa1",
            "Tarefa2": "Pessoa2"
        },
        "Coluna2": {
            "Tarefa1": "Pessoa3"
        }
    }
              

Tendo em vista que o nome do kanban será o nome do arquivo,
cada kanban terá no mínimo 2 colunas,
inicialmente as colunas não terão tarefas,
cada coluna poderá ter várias tarefas,
cada tarefa terá apenas uma pessoa responsável.
'''

import os
import json


def criar_kanban(nome_kanban:str, nome_colunas:list[str]) -> None:
    '''
    Cria um kanban com o nome, quantidade de colunas (mínimo 2) e nomes das colunas.
    '''
    # Tratamento de erro
    if not os.path.exists("KANBANS"):
        os.makedirs("KANBANS/")        
    try:
        # Verificando se o kanban ja existe
        if nome_kanban in os.listdir("KANBANS"):
            raise Exception("Ja existe um kanban com esse nome.")
    # Tratamento de exceção
    except Exception as e:
        return e
    # Caso não haja erro
    else:
        with open(f"KANBANS/{nome_kanban}.json", 'w', encoding="utf-8") as f:
            json.dump({coluna: {} for coluna in nome_colunas}, f, indent=4)


def ler_kanban(nome_kanban:str) -> dict[str, dict[str: str]]:
    '''
    Le o kanban com o nome.
    '''
    if os.path.exists(f"KANBANS/{nome_kanban}.json"):
        with open(f"KANBANS/{nome_kanban}.json", 'r', encoding="utf-8") as f:
            return json.load(f)
    else:
        return None


def atualizar_kanban(nome_kanban:str, kanban:dict[str: dict[str: str]]) -> None:
    '''
    Atualiza os dados modificados de um kanban.
    '''
    with open(f"KANBANS/{nome_kanban}.json", 'w', encoding="utf-8") as f:
        json.dump(kanban, f, indent=4)


def deletar_kanban(nome_kanban:str) -> bool:
    '''
    Deleta um kanban com o nome.
    '''
    if nome_kanban in os.listdir("KANBANS"):
        os.remove(f"KANBANS/{nome_kanban}.json")
        return True
    else:
        return False


def adicionar_coluna(nome_kanban:str, nome_coluna:str = None) -> bool:
    '''
    Adiciona uma coluna ao kanban com o nome.
    '''
    kanban = ler_kanban(nome_kanban)
    if kanban is None:
        return False
    
    if not nome_coluna:
        kanban[f"Coluna{len(kanban.keys()) + 1}"] = {}
    elif nome_coluna in kanban.keys():
        return False
    else:
        kanban[nome_coluna] = {}
    
    atualizar_kanban(nome_kanban, kanban)
    return True
    

def deletar_coluna(nome_kanban:str, nome_coluna:str) -> bool:
    '''
    Deleta uma coluna do kanban.
    '''
    kanban = ler_kanban(nome_kanban)
    if kanban is None:
        return False
    
    if kanban.pop(nome_coluna, None):
        atualizar_kanban(nome_kanban, kanban)
        return True
    else:
        return False


def adicionar_tarefa(nome_kanban:str, nome_coluna:str, nome_tarefa:str, pessoa_responsavel:str) -> bool:
    '''
    Adiciona uma tarefa e seu responsável a uma coluna do kanban.
    '''
    kanban = ler_kanban(nome_kanban)
    if kanban is None:
        return False
    
    if nome_coluna in kanban.keys():
        if nome_tarefa in kanban[nome_coluna].keys():
            return False
        else:
            kanban[nome_coluna][nome_tarefa] = pessoa_responsavel
            atualizar_kanban(nome_kanban, kanban)
            return True
    else:
        return False
    

def deletar_tarefa(nome_kanban:str, nome_coluna:str, nome_tarefa:str) -> bool:
    '''
    Deleta uma tarefa de uma coluna do kanban.
    '''
    kanban = ler_kanban(nome_kanban)
    if kanban is None:
        return False
    
    if kanban[nome_coluna].pop(nome_tarefa, None):
        atualizar_kanban(nome_kanban, kanban)
        return True
    else:
        return False