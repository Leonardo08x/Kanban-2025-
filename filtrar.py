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
                ft.Text('🔎TELA DE PESQUISA🔎',
                        style=ft.TextStyle(

                                    size=32,
                                    font_family="Kanit",
                                    weight=ft.FontWeight.BOLD,
                                    foreground=ft.Paint(
                                        gradient=ft.PaintLinearGradient(
                                            (2000, 150),
                                            (150, 2000),
                                            [ft.Colors.INVERSE_PRIMARY, ft.Colors.PURPLE_200]
                                        )
                                    ),
                                )),
                ft.Row(controls=caixa_de_filtros()),
                ft.Column(
                    scroll=ft.ScrollMode.AUTO,
                    width=1700,
                    height=900,
                    controls=[
                        ft.Row(
                            expand=True,
                            spacing=20,
                            wrap=True,
                            controls=[
                                gerenciamento.criar_cartao_do_kanban(kanban.get('nome'))
                                for kanban in carregar_kanbans()
                            ]
                        )
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
                ft.Text('Filtrar por nome do kanban',style=ft.TextStyle(

                                    size=16,
                                    font_family="Kanit",
                                    weight=ft.FontWeight.BOLD,
                                    foreground=ft.Paint(
                                        gradient=ft.PaintLinearGradient(
                                            (2000, 150),
                                            (150, 2000),
                                            [ft.Colors.INVERSE_PRIMARY, ft.Colors.PURPLE_200]
                                        )
                                    ),
                                )),
                ft.ElevatedButton(
                    text='Selecionar todos',
                    on_click=all_filtros_kanban,
                    icon=ft.Icons.SELECT_ALL,
                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.DEEP_PURPLE_500,
                    )
                ),
                ft.Divider(),
                ft.GridView(
                    width=400,
                    height=200,
                    controls=[
                        ft.Column(
                            controls=filtro_nome_kanban(),
                            scroll=ft.ScrollMode.ALWAYS
                        )
                    ],
                ),
            ],
        ),
        ft.Column(
            controls=[
                ft.Text('Filtrar por nome da coluna',style=ft.TextStyle(

                                    size=16,
                                    font_family="Kanit",
                                    weight=ft.FontWeight.BOLD,
                                    foreground=ft.Paint(
                                        gradient=ft.PaintLinearGradient(
                                            (2000, 150),
                                            (150, 2000),
                                            [ft.Colors.INVERSE_PRIMARY, ft.Colors.PURPLE_200]
                                        )
                                    ),
                                )),
                ft.ElevatedButton(
                    text='Selecionar todos',
                    on_click=all_filtros_coluna,
                    icon=ft.Icons.SELECT_ALL,
                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.DEEP_PURPLE_500,
                    )
                ),
                ft.Divider(),
                ft.GridView(
                    width=400,
                    height=200,
                    controls=[
                        ft.Column(
                            controls=filtro_nome_coluna(),
                            scroll=ft.ScrollMode.ALWAYS
                        )
                    ],
                ),
            ],
        ),
        ft.Column(
            controls=[
                ft.Text('Filtrar por responsavel',style=ft.TextStyle(

                                    size=16,
                                    font_family="Kanit",
                                    weight=ft.FontWeight.BOLD,
                                    foreground=ft.Paint(
                                        gradient=ft.PaintLinearGradient(
                                            (2000, 150),
                                            (150, 2000),
                                            [ft.Colors.DEEP_PURPLE_50, ft.Colors.PURPLE_200]
                                        )
                                    ),
                                )),
                ft.TextField(
                    border_color=ft.Colors.PURPLE,
                    bgcolor=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.Colors.DEEP_PURPLE,
                    label_style=ft.TextStyle(
                        color=ft.Colors.DEEP_PURPLE,
                        decoration=ft.TextDecoration.UNDERLINE,
                        decoration_color=ft.Colors.DEEP_PURPLE,
                        size=15,
                        italic=True),
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
            on_change=filtrar_kanban,
            fill_color=ft.Colors.PURPLE_200,
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
            on_change=filtrar_coluna,
            fill_color=ft.Colors.PURPLE_200,
        )
        for coluna in sorted(list(nomes_colunas))
    ]

############################## botao filtros ################################
def botao_aplicar_filtros():
    return ft.ElevatedButton(
        text='Aplicar Filtros',
        on_click=lambda e: con.atualizar_pagina(conteudo()),
        icon=ft.Icons.SEARCH,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.PURPLE,
        )
    )

######################################## setor nome kanban #########################################
def filtrar_kanban(e):
    global filtro_kanban
    # caixa = e.control -> acessa a caixa de filtros
    # column = e.control.parent -> acessa a coluna que contem a caixa de filtros
    column = e.control.parent
    
    # os checkboxes estao dentro da coluna
    checkboxes = column.controls
    # checkbox marcados
    nomes_marcados = [nome.label for nome in checkboxes if nome.value]

    # criando o filtro
    if nomes_marcados:
        filtro_kanban = lambda kanban: kanban.get('nome') in nomes_marcados
    else:
        filtro_kanban = None


def all_filtros_kanban(e):
    global filtro_kanban
    # botao = e.control -> acessa o botao
    # column_externa = e.control.parent -> acessa a coluna que contem o botao
    # gridview = e.control.parent.controls[3] -> acessa a gridview que contem a coluna de filtros
    # column_caixas = e.control.parent.controls[3].controls[0] -> acessa a coluna que contem a caixa de filtros
    column_caixas = e.control.parent.controls[3].controls[0]
    
    # os checkboxes estao dentro da coluna
    checkboxes = column_caixas.controls

    # marca todos os checkboxes
    for checkbox in checkboxes:
        checkbox.value = True

    # limpa a variavel filtro
    filtro_kanban = None
    
    con.page.update()




######################################## setor nome coluna #########################################

def filtrar_coluna(e):
    global filtro_coluna
    # caixa = e.control -> acessa a caixa de filtros
    # column = e.control.parent -> acessa a coluna que contem a caixa de filtros
    column = e.control.parent

    # os checkboxes estao dentro da coluna
    checkboxes = column.controls
    # checkbox marcados
    filtro = [nome.label for nome in checkboxes if nome.value]

    # criando o filtro
    if filtro:
        filtro_coluna = lambda kanban: any(coluna.get('nome') in filtro for coluna in kanban.get('colunas'))
    else:
        filtro_coluna = None


def all_filtros_coluna(e):
    global filtro_coluna
    # botao = e.control -> acessa o botao
    # column_externa = e.control.parent -> acessa a coluna que contem o botao
    # gridview = e.control.parent.controls[3] -> acessa a gridview que contem a coluna de filtros
    # column_caixas = e.control.parent.controls[3].controls[0] -> acessa a coluna que contem a caixa de filtros
    column_caixas = e.control.parent.controls[3].controls[0]

    # os checkboxes estao dentro da coluna
    checkboxes = column_caixas.controls

    # marca todos os checkboxes
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

