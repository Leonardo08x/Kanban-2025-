import flet as ft
import controle as con
from lista_de_cores import cores
from bd import bd


def visualizar_kanban(index : int) -> list:
    return [
        ft.Column(
            controls=[
                ft.Text(f'Tela visualizar kanban: {bd[index]["nome"]}'),
                ft.Row(
                    controls=[
                        carregar_cartao_da_coluna(coluna)
                        for coluna in bd[index].get('colunas')
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.START
        )
    ]


def carregar_cartao_da_coluna(coluna : dict[str, list[tuple[str, str]]]) -> ft.Column:
    return ft.Column(
        controls=[
            ft.Container(
            width=250,
            height=150,
            bgcolor=cores.get(coluna.get('cor')),
            padding = 20,
            border=ft.border.all(2, ft.Colors.DEEP_PURPLE_500),
            border_radius=10,
            expand=True,
            content=ft.Column(
                controls=[
                    # título com nome da coluna
                    ft.TextField(
                        value=coluna.get('nome'),
                        label="nome coluna",
                        expand=True,
                        text_style=ft.TextStyle(
                            color=ft.Colors.WHITE,
                            size=25,
                            italic=True,
                            ),
                        disabled=True,
                        border="none",
                        ),
                    ],
                ),
            ),
        ] + [
            carregar_tarefas(coluna.get('cor'), tarefa)
                        for tarefa in coluna.get('tarefas')
        ],
        alignment=ft.MainAxisAlignment.START
    )


def carregar_tarefas(cor, tarefa : tuple[str, str]) -> ft.Container:
    return ft.Container(
        width=250,
        height=100,
        bgcolor=cores.get(cor),
        padding = 10,
        border=ft.border.all(2, ft.Colors.DEEP_PURPLE_500),
        border_radius=10,
        expand=True,
        content=ft.TextField(
            value=f"{tarefa[0]}: {tarefa[1]}",
            label="responsavel: tarefa",
            text_style=ft.TextStyle(
                color=ft.Colors.WHITE,
                size=17,
            ),
            disabled=True,
            border="none",
        )
    )
                


