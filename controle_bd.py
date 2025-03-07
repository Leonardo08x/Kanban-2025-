# controle_bd.py é o módulo que contém as funções para tratamento de erro e chamada das funções do bd.py

import os
import bd

def criar():
    '''
    Lista com nomes das colunas
    '''
    nome_kanban = input("Digite o nome do kanban: ").capitalize()
    colunas = input("Digite a quantidade de colunas (mínimo 2): ")
    # Alterando a quantidade de colunas para no mínimo 2
    if not colunas.isdigit():
        print("Digite um número inteiro para a quantidade de colunas.", end='\n\n')
    else:
        colunas = int(colunas)
        if colunas < 2:
            colunas = 2
        lista_colunas = []  # Lista com nome das colunas
        # Adicionando o nome das colunas à lista
        while len(lista_colunas) < colunas:
            nome_coluna = input(f"Digite o nome da coluna {len(lista_colunas) + 1}: ").capitalize()
            if nome_coluna in lista_colunas:
                print("Coluna já existe.", end='\n\n')
                continue
            else:
                lista_colunas.append(nome_coluna)
        # Criando o kanban
        kanban = bd.criar_kanban(nome_kanban, lista_colunas)
        if kanban is None:
            print("Kanban criado com sucesso.", end='\n\n')
        else:
            print("Erro ao criar o kanban.", kanban, end='\n\n')


def verificar_kanban():
    '''
    Função que verifica se existe a pasta KANBANS e se há arquivos dentro dela
    '''
    if os.path.exists("KANBANS") and os.listdir("KANBANS"):
        return True
    else:
        print("Nenhum kanban encontrado.", end='\n\n')
        return False

    
def deletar():
    '''
    Função que deleta um kanban
    '''
    if verificar_kanban(): # Verifica se existe algum kanban no bd
        nome_kanban = input("Digite o nome do kanban: ").capitalize()
        if bd.deletar_kanban(nome_kanban):
            print("Kanban deletado com sucesso.", end='\n\n')
        else:
            print("Kanban não encontrado.", end='\n\n')


def visualizar():
    '''
    Função que visualiza um kanban
    '''
    if verificar_kanban(): # Verifica se existe algum kanban no bd
        nome_kanban = input("Digite o nome do kanban: ").capitalize()
        # Carrega o kanban do bd
        kanban = bd.ler_kanban(nome_kanban)
        if kanban is None:
            print("Kanban não encontrado.")
        else:
            print(kanban, end='\n\n')


def listar():
    '''
    Função que lista todos os kanbans disponíveis
    '''
    if verificar_kanban(): # Verifica se existe algum kanban no bd
        for arquivo in os.listdir("KANBANS"):
            # Verifica se o arquivo é um json
            if arquivo.endswith(".json"):
                arquivo = arquivo.replace('.json', '') # Renomeando o arquivo
                print(f"Nome: {arquivo}")
                kanban = bd.ler_kanban(arquivo)
                print(kanban, end='\n\n')


def editar():
    '''
    Função que edita um kanban
    '''
    if verificar_kanban(): # Verifica se existe algum kanban no bd
        nome_kanban = input("Digite o nome do kanban: ").capitalize()
        kanban = bd.ler_kanban(nome_kanban) # Carrega o kanban do bd
        # Verifica se o kanban existe
        if kanban is None:
            print("Kanban não encontrado.")
        # Caso exista, chama as outras funções de edição
        else:
            while True:
                # Menu de edição
                opcao = input("0 - Sair\n1 - Adicionar coluna\n2 - Remover coluna\n3 - Adicionar tarefa\n4 - Remover tarefa\n\nEscolha: ")
                if opcao == '0':
                    break
                elif opcao == '1':
                    editar_adicionar_coluna(nome_kanban, kanban)
                elif opcao == '2':
                    editar_deletar_coluna(nome_kanban, kanban)
                elif opcao == '3':
                    editar_adicionar_tarefa(nome_kanban, kanban)
                elif opcao == '4':
                    editar_deletar_tarefa(nome_kanban, kanban)
                else:
                    print("Opção inválida.", end='\n\n')


def editar_adicionar_coluna(nome_kanban:str, kanban:dict):
    '''
    Função que adiciona uma nova coluna ao kanban
    '''
    nome_coluna = input("Digite o nome da coluna: ").capitalize()
    # Verifica se a coluna já existe
    if nome_coluna in kanban.keys():
        print("Coluna ja existe.", end='\n\n')
    # Caso não exista, adiciona a nova coluna ao kanban
    else:
        if bd.adicionar_coluna(nome_kanban, nome_coluna):
            print("Coluna adicionada com sucesso.", end='\n\n')
        else:
            print("Erro ao adicionar coluna.", end='\n\n')


def editar_deletar_coluna(nome_kanban:str, kanban:dict):
    '''
    Função que deleta uma coluna do kanban
    '''
    # Verifica se o kanban tem mais de duas colunas, caso contrário, não é possível deletar uma coluna
    if len(kanban.keys()) == 2:
        print("Kanban deve ter ao menos duas colunas.", end='\n\n')
    # Caso tenha mais de duas colunas, deleta a coluna escolhida
    nome_coluna = input("Digite o nome da coluna: ").capitalize()
    if bd.deletar_coluna(nome_kanban, nome_coluna):
        print("Coluna removida com sucesso.", end='\n\n')
    else:
        print("Erro ao remover coluna.", end='\n\n')

    
def editar_adicionar_tarefa(nome_kanban:str, kanban:dict):
    '''
    Função que adiciona uma nova tarefa ao kanban
    '''
    nome_coluna = input("Digite o nome da coluna: ").capitalize()
    # Verifica se a coluna existe no kanban
    if nome_coluna not in kanban.keys():
        print("Coluna não encontrada.", end='\n\n')
    # Caso exista, adiciona a nova tarefa à coluna
    else:
        tarefa = input("Digite o nome da tarefa: ").capitalize()
        # Verifica se a tarefa ja existe
        if tarefa in kanban[nome_coluna].keys():
            print("Tarefa ja existe.", end='\n\n')
        # Caso não exista, adiciona a nova tarefa à coluna selecionada
        else:
            # Adiciona a pessoa responsável pela tarefa
            pessoa_responsavel = input("Digite o nome da pessoa responsável: ").title()
            # Adiciona a tarefa e seu responsável ao kanban
            if bd.adicionar_tarefa(nome_kanban, nome_coluna, tarefa, pessoa_responsavel):
                print("Tarefa adicionada com sucesso.", end='\n\n')
            else:
                print("Erro ao adicionar tarefa.", end='\n\n')


def editar_deletar_tarefa(nome_kanban:str, kanban:dict):
    '''
    Função que deleta uma tarefa do kanban
    '''
    nome_coluna = input("Digite o nome da coluna: ").capitalize()
    # Verifica se a coluna existe no kanban
    if nome_coluna not in kanban.keys():
        print("Coluna não encontrada.", end='\n\n')
    # Verifica se a coluna está vazia
    elif not kanban[nome_coluna]:
        print("Coluna vazia.", end='\n\n')
    # Caso exista e não esteja vazia, poderá remover a tarefa selecionada
    else:
        tarefa = input("Digite o nome da tarefa: ").capitalize()
        # Verifica se a tarefa existe na coluna
        if tarefa not in kanban[nome_coluna].keys():
            print("Tarefa não encontrada.", end='\n\n')
        # Caso exista, remove a tarefa da coluna
        else:
            if bd.deletar_tarefa(nome_kanban, nome_coluna, tarefa):
                print("Tarefa removida com sucesso.", end='\n\n')
            else:
                print("Erro ao remover tarefa.", end='\n\n')
