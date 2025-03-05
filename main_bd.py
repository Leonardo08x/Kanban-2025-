import os
import json

KANBANS = {}

def carregar_kanban():
    global KANBANS
    for arquivo in os.listdir("KANBANS"):
        with open(f"KANBANS/{arquivo}", 'r', encoding="utf-8") as f:
            KANBANS[os.path.splitext(arquivo)[0]] = json.load(f)


def salvar_kanbans():
    for kanban, colunas in KANBANS.items():
        with open(f"KANBANS/{kanban}.json", 'w', encoding="utf-8") as f:
            json.dump(colunas, f, indent=4)


def criar_kanban():
    nome = input('Digite o nome do kanban: ').capitalize()
    if KANBANS.get(nome, False):
        print('Kanban já existe.')
        return False

    try:
        num_colunas = int(input('Digite o número de colunas do kanban (min 2 colunas): '))
        if num_colunas < 2:
            print('Número mínimo de colunas é 2.')
            return False
    except ValueError:
        print("Entrada inválida. Digite apenas números.")
        return False

    colunas = {}
    for i in range(num_colunas):
        coluna = input(f'Digite o nome da coluna {i + 1}: ').capitalize()
        colunas[coluna] = []

    KANBANS[nome] = colunas

    with open(f"KANBANS/{nome}.json", 'w', encoding="utf-8") as f:
        json.dump(colunas, f, indent=4)

    print(f'Kanban {nome} criado com sucesso.')


def deletar_kanban():
    for kanban in KANBANS.keys():
        print(kanban)

    nome = input('Digite o nome do kanban: ').capitalize()
    if KANBANS.pop(nome, False):
        print(f"Kanban {nome} deletado com sucesso.")
        os.remove(f"KANBANS/{nome}.json")
    else:
        print('Kanban não encontrado.')

    
def listar_kanban():
    for kanban, colunas in KANBANS.items():
        print('\n' + kanban)
        for coluna, pessoas in colunas.items():
            print(f"{coluna}: {', '.join(pessoas)}")


def editar_kanban():
    nome = input('Digite o nome do kanban: ').capitalize()
    kanban = KANBANS.get(nome, False)
    if kanban:
        coluna = input('Digite o nome da coluna: ').capitalize()
        if coluna:
            opcao = input("Editar nome da coluna (c)\nAdicionar pessoa da coluna (p)\nRetirar pessoa da coluna (r)\nResposta: ")
            if opcao.lower() == 'c':
                nova_coluna = input("Novo nome da coluna: ").capitalize()
                if kanban.get(nova_coluna, False):
                    print("Já existe uma coluna com esse nome.")
                    return False
                else:
                    kanban[nova_coluna] = kanban.pop(coluna)
                    return True
            elif opcao.lower() == 'p':
                nova_pessoa = input("Nome da nova pessoa: ").title()
                kanban.get(coluna).append(nova_pessoa)
                return True
            elif opcao.lower() == 'r': 
                if kanban.get(coluna):
                    pessoa = input("Nome da pessoa: ").title()
                    kanban.get(coluna).pop(pessoa, print("erro: pessoa não encontrada."))
                    return True
                else:
                    print("Não há pessoas nesta coluna.")
                    return False
            else:
                print("Opção inválida.")
        else:
            print("Coluna não encontrada.")            
    else:
        print('Kanban não encontrado.')


menu = '''
(0) Parar
(1) Criar novo Kanban
(2) Deletar Kanban
(3) Editar Kanban
(4) Listar Kanbans
(5) Carregar Kanbans
Resposta: '''

carregar_kanban()
while True:
    opcao = input(menu)
    
    if opcao == '0':
        break

    elif opcao == '1':
        criar_kanban()

    elif opcao == '2':
        deletar_kanban()

    elif opcao == '3':
        if editar_kanban():
            salvar_kanbans()
            print("Kanban editado com sucesso.")

    elif opcao == '4':
        listar_kanban()

    elif opcao == '5':
        salvar_kanbans()
        print("Kanbans salvos.")

    else:
        print("Opção inválida.")
