import flet as ft
import controle as con
from bd import bd


def conteudo() -> list:
    global botoes
    return [
        ft.Column(
            controls=[
                ft.Text('Tela pesquisa'),
                ft.Row(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text('Filtro nome kanban'),
                                ft.Container(
                                    content=ft.Row(filtro_nome_kanban())
                                ),
                                botoes
                            ]
                        ),
                        ft.Column(
                            controls=[
                                ft.Text('Filtro nome coluna'),
                                ft.Container(
                                    content=ft.Row(filtro_nome_coluna())
                                ),
                                botoes
                            ]
                        ),
                        ft.Column(
                            controls=[
                                ft.Text('Filtro responsavel'),
                                ft.TextField(
                                    on_change=filtrar
                                )
                            ]
                        )
                    ],

                )
            ]
        )
    ]


def carregar_nome_kanbans(nomes_kanbans : list = None):
    if nomes_kanbans:
        return [kanban for kanban in bd if kanban.get('nome') in nomes_kanbans]
    else:
        return bd


def carregar_nome_colunas(nome_colunas : list = None):
    if nome_colunas:
        kanbans = []
        for kanban in bd:
            for coluna in kanban.get('colunas'):
                if coluna.get('nome') in nome_colunas:
                    kanbans.append(kanban)
                    break
        return kanbans
    else:
        return bd        


def carregar_nome_responsabel(responsavel : str = None):
    if responsavel:
        kanbans = []
        for kanban in bd:
            for coluna in kanban.get('colunas'):
                for tarefa in coluna.get('tarefas'):
                    if tarefa[0].startswith(responsavel):
                        kanbans.append(kanban)
                        break
        return kanbans
    else:
        return bd
    

def filtro_nome_kanban() -> list:
    return [
        ft.Checkbox(
            label=kanban.get('nome'),
            value=False,

        )
        for kanban in bd
    ]


def filtro_nome_coluna() -> list:
    nomes_colunas = set(
        [
            coluna.get('nome')
            for kanban in bd
            for coluna in kanban.get('colunas')
        ]
    )
    return [
        ft.Checkbox(
            label=coluna,
            value=False,

        )
        for coluna in nomes_colunas
    ]


def limpar_filtros(e):
    pass


def filtrar(e):
    pass


# variaveis globais
botoes = ft.Row(
    controls=[
        ft.ElevatedButton(
        text='Limpar filtros',
        on_click=limpar_filtros
        ),
        ft.ElevatedButton(
        text='Filtrar',
        on_click=filtrar
        )
    ]
)