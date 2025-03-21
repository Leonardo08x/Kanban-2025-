import flet as ft
import controle as con


import gerenciamento
# variaveis globais
filtro_kanban = []
filtro_coluna = []
filtro_responsavel = []


def conteudo() -> list:
    global botoes
    return [
        ft.Column(
            controls=[
                ft.Text('Tela pesquisa'),
                ft.Row(controls=caixa_de_filtros()),
                ft.Row(
                    controls=[
                        # cria um cartão com o nome do kanban
                        # TODO retirar os botões de editar e apagar, manter apenas o botão de acesso
                        gerenciamento.criar_cartao_do_kanban(kanban.get('nome'))
                        for kanban in carregar_kanbans()
                    ]
                )
            ]
        )
    ]


################################## funções auxiliares do conteudo ##################################
# conteudo que contem as caixas de filtros, aparece na tela de pesquisa
def caixa_de_filtros() -> list:
    return [
        ft.Column(
            controls=[
                ft.Text('Filtro nome kanban'),
                ft.ElevatedButton(
                    text='Limpar filtros',
                    on_click=limpar_filtros_kanban
                ),
            ] + filtro_nome_kanban(),
        ),
        ft.Column(
            controls=[
                ft.Text('Filtro nome coluna'),
                ft.ElevatedButton(
                    text='Limpar filtros',
                    on_click=limpar_filtros_coluna
                ),
            ] + filtro_nome_coluna(),
        ),
        ft.Column(
            controls=[
                ft.Text('Filtro responsavel'),
                ft.TextField(
                    on_change=filtrar_responsavel
                )
            ]
        )
    ]

def carregar_kanbans() -> list:
    return [
        kanban
        for kanban in con.bd
        if kanban in filtro_kanban and\
            kanban in filtro_coluna and\
            kanban in filtro_responsavel
    ]
    
############################################ Checkboxs #############################################
# retorna a lista de todos os nomes dos kanbans
def filtro_nome_kanban() -> list:
    return [
        ft.Checkbox(
            label=kanban.get('nome'),
            value=False,
            on_change=filtrar_kanban
        )
        for kanban in con.bd
    ]


# retorna a lista de todos os nomes das colunas
def filtro_nome_coluna() -> list:
    nomes_colunas = {
        coluna.get('nome')
        for kanban in con.bd
        for coluna in kanban.get('colunas')
    }
    return [
        ft.Checkbox(
            label=coluna,
            value=False,
            on_change=filtrar_coluna
        )
        for coluna in sorted(list(nomes_colunas))
    ]


######################################## setor nome kanban #########################################

def filtrar_kanban(e) -> list[dict[str, str | list[dict[str, str |list[tuple[str, str]]]]]]:
    global filtro_kanban
    # botão esta dentro de uma coluna
    column = e.control.parent
    # os checkboxes estao dentro da coluna a partir da posicao 2
    checkboxes = column.controls[2:]
    # checkbox marcados
    filtro = [nome.label for nome in checkboxes if nome.value]
    if filtro:
        # kanbans que atendem o filtro
        filtro_kanban = [
            kanban
            for kanban in con.bd
            if kanban.get('nome') in filtro
        ]
        # atualiza a pagina
        con.page.update()
    # caso nenhum checkbox esteja marcado limpa os filtros
    else:
        limpar_filtros_kanban(e)


def limpar_filtros_kanban(e):
    global filtro_kanban
    # botão esta dentro de uma coluna
    column = e.control.parent
    # os checkboxes estao dentro da coluna a partir da posicao 2
    checkboxes = column.controls[2:]
    # desmarca os checkboxes
    for checkbox in checkboxes:
        checkbox.value = False
    # limpa a variavel filtro
    filtro_kanban = []
    # atualiza a coluna
    column.update()


######################################## setor nome coluna #########################################

def filtrar_coluna(e) -> list[dict[str, str | list[dict[str, str | list[tuple[str, str]]]]]]:
    global filtro_coluna
    # botão esta dentro de uma coluna
    column = e.control.parent
    # os checkboxes estao dentro da coluna a partir da posicao 2
    checkboxes = column.controls[2:]
    # checkbox marcados
    filtro = [nome.label for nome in checkboxes if nome.value]
    if filtro:
        # kanbans que atendem o filtro
        kanbans = []
        for kanban in con.bd:
            for coluna in kanban.get('colunas'):
                if coluna.get('nome') in filtro and not kanban in kanbans:
                    kanbans.append(kanban)
        filtro_coluna = kanbans
        # atualiza a pagina
        con.page.update()
    # caso nenhum checkbox esteja marcado limpa os filtros
    else:
        limpar_filtros_coluna(e)


def limpar_filtros_coluna(e):
    global filtro_coluna
    # botão esta dentro de uma coluna
    column = e.control.parent
    # os checkboxes estao dentro da coluna a partir da posicao 2
    checkboxes = column.controls[2:]
    # desmarca os checkboxes
    for checkbox in checkboxes:
        checkbox.value = False
    # limpa a variavel filtro
    filtro_coluna = []
    # atualiza a coluna
    column.update()


#################################### setor nome rersponsavel #######################################

def filtrar_responsavel(e) -> list[dict[str, str | list[dict[str, str |list[tuple[str, str]]]]]]:
    global filtro_responsavel
    # captura o texto no textfield
    responsavel = e.control.value

    # kanbans que atendem o filtro
    kanbans = []
    for kanban in con.bd:
        for coluna in kanban.get('colunas'):
            for tarefa in coluna.get('tarefas'):
                if tarefa[0].startswith(responsavel) and not kanban in kanbans:
                    kanbans.append(kanban)
    filtro_responsavel = kanbans
    # atualiza a pagina
    con.page.update()

