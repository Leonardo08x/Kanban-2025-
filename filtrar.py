import re
import flet as ft
import controle as con
import banco_de_dados as bd


import gerenciamento
# variaveis globais
filtro_kanban = None
filtro_coluna = None
filtro_responsavel = None


def conteudo() -> list:
    return [
        ft.Column(
            controls=[
                ft.Text('Tela pesquisa'),
                ft.Row(controls=caixa_de_filtros()),
                ft.Row(
                    controls=[
                        gerenciamento.criar_cartao_do_kanban(kanban.get('nome'))
                        for kanban in carregar_kanbans()
                    ]
                )
            ]
        )
    ]


################################## funções auxiliares do conteudo ##################################
def caixa_de_filtros() -> list[ft.Column]:
    return [
        ft.Column(
            controls=[
                ft.Text('Filtro nome kanban'),
                ft.ElevatedButton(
                    text='Selecionar todos',
                    on_click=all_filtros_kanban
                ),
                ft.Divider(),
                ft.GridView(
                    runs_count=3,
                    width=300,
                    height=150,
                    controls=filtro_nome_kanban()
                )
            ],
        ),
        ft.Column(
            controls=[
                ft.Text('Filtro nome coluna'),
                ft.ElevatedButton(
                    text='Selecionar todos',
                    on_click=all_filtros_coluna
                ),
                ft.Divider(),
                ft.GridView(
                    runs_count=6,
                    width=600,
                    height=150,
                    controls=filtro_nome_coluna()
                )
            ],
        ),
        ft.Column(
            controls=[
                ft.Text('Filtro responsavel'),
                ft.TextField(
                    on_change=filtrar_responsavel
                ),
                botao_aplicar_filtros()
            ]
        ),
    ]


def carregar_kanbans() -> list[dict[str, str | list[dict[str, str | list[tuple[str, str]]]]]]:
    global filtro_kanban, filtro_coluna, filtro_responsavel
    # veificando quais filtros foram marcados
    filtros = [filtro for filtro in [filtro_kanban, filtro_coluna, filtro_responsavel] if filtro is not None] 
    # filtrando os kanbans
    kanbans_filtrados = list(filter(lambda kanban: any(filtro(kanban) for filtro in filtros) if filtros else True, con.bd))
    # limpando os filtros
    filtro_kanban = None
    filtro_coluna = None
    filtro_responsavel = None
    # retornando os kanbans filtrados
    return kanbans_filtrados
    
############################################ Checkboxs #############################################
# retorna a lista de todos os nomes dos kanbans
def filtro_nome_kanban() -> list[ft.Checkbox]:
    return [
        ft.Checkbox(
            label=kanban.get('nome'),
            on_change=filtrar_kanban
        )
        for kanban in con.bd
    ]


# retorna a lista de todos os nomes das colunas
def filtro_nome_coluna() -> list[ft.Checkbox]:
    nomes_colunas = {
        coluna.get('nome')
        for kanban in con.bd
        for coluna in kanban.get('colunas')
    }
    return [
        ft.Checkbox(
            label=coluna,
            on_change=filtrar_coluna
        )
        for coluna in sorted(list(nomes_colunas))
    ]

############################## botao filtros ################################
def botao_aplicar_filtros():
    return ft.ElevatedButton(
        text='Aplicar Filtros',
        on_click=lambda e: con.atualizar_pagina(conteudo()),
    )

######################################## setor nome kanban #########################################

def filtrar_kanban(e):
    global filtro_kanban
    # caixa = e.control -> acessa a caixa de filtros
    # gridview = e.control.parent -> acessa a gridview que contem a caixa de filtros
    grideview = e.control.parent
    
    # os checkboxes estao dentro da gridview
    checkboxes = grideview.controls
    # checkbox marcados
    nomes_marcados = [nome.label for nome in checkboxes if nome.value]

    # criando o filtro
    if nomes_marcados:
        filtro_kanban = lambda kanban: kanban.get('nome') in nomes_marcados
    else:
        filtro_kanban = None


def all_filtros_kanban(e):
    global filtro_kanban
    # caixa = e.control -> acessa a caixa de filtros
    # column = e.control.parent -> acessa a coluna que contem a caixa de filtros
    # gridview = e.control.parent.controls[3] -> acessa a gridview que contem a caixa de filtros
    gridview = e.control.parent.controls[3]
    # os checkboxes estao dentro da gridview
    checkboxes = gridview.controls
    # desmarca os checkboxes
    for checkbox in checkboxes:
        checkbox.value = True
    # limpa a variavel filtro
    filtro_kanban = None
    
    con.page.update()




######################################## setor nome coluna #########################################

def filtrar_coluna(e):
    global filtro_coluna
    # caixa = e.control -> acessa a caixa de filtros
    # gridview = e.control.parent -> acessa a gridview que contem a caixa de filtros
    gridview = e.control.parent
    # os checkboxes estao dentro da gridview
    checkboxes = gridview.controls
    # checkbox marcados
    filtro = [nome.label for nome in checkboxes if nome.value]

    # criando o filtro
    if filtro:
        filtro_coluna = lambda kanban: any(coluna.get('nome') in filtro for coluna in kanban.get('colunas'))
    else:
        filtro_coluna = None


def all_filtros_coluna(e):
    global filtro_coluna
    # caixa = e.control -> acessa a caixa de filtros
    # column = e.control.parent -> acessa a coluna que contem a caixa de filtros
    # gridview = e.control.parent.controls[3] -> acessa a gridview que contem a caixa de filtros
    gridview = e.control.parent.controls[3]
    # os checkboxes estao dentro da gridview
    checkboxes = gridview.controls
    # desmarca os checkboxes
    for checkbox in checkboxes:
        checkbox.value = True
    # limpa a variavel filtro
    filtro_coluna = None
    
    con.page.update()


#################################### setor nome responsavel #######################################
def remover_acentos(texto : str) -> str:
    texto_a = re.sub(r'[áàâã]', 'a', texto)
    texto_e = re.sub(r'[éèê]', 'e', texto_a)
    texto_i = re.sub(r'[íìî]', 'i', texto_e)
    texto_o = re.sub(r'[óòôõ]', 'o', texto_i)
    texto_u = re.sub(r'[úùû]', 'u', texto_o)
    texto_c = re.sub(r'[ç]', 'c', texto_u)
    return texto_c
    
    
def filtrar_responsavel(e):
    global filtro_responsavel
    # captura o texto no textfield
    responsavel = e.control.value

    if not responsavel:
        filtro_responsavel = None

    else:
        # tratando valores
        responsavel = remover_acentos(responsavel).lower()

        # criando o filtro
        filtro_responsavel = lambda kanban: any(
            remover_acentos(tarefas[0]).lower().startswith(responsavel)
            for coluna in kanban.get('colunas')
            for tarefas in coluna.get('tarefas')
        )

