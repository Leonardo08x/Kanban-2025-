import flet as ft
import controle as con
from bd import bd


def conteudo() -> list:
    return [
        ft.Column(
            controls=[
                ft.Text('Tela gerenciamento'),
                ft.Row(
                    controls=[
                        criar_cartao_do_kanban(kanban.get('nome'))
                        for kanban in bd
                    ]
                )
            ]
        ),
    ]


def criar_cartao_do_kanban(nome_do_kanban):
    return ft.Container(
        width=250,
        height=150,
        bgcolor=ft.Colors.PURPLE,
        padding = 20,
        border=ft.border.all(2, ft.Colors.DEEP_PURPLE_500),
        border_radius=10,
        expand=True,
        content=ft.Column(
            controls=[
                # título com nome do kanban
                ft.Text(
                    value=nome_do_kanban,
                    expand=True,
                    style=ft.TextStyle(
                        color=ft.Colors.WHITE,
                        size=32,
                        italic=True,
                    ),
                ),
                # botões
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="Excluir",
                            on_click=apagar_kanban,
                        ),
                        ft.ElevatedButton(
                            text="Editar",
                            on_click=editar_kanban
                        ),
                        # botão de acesso ao kanban
                        ft.TextButton(
                            "GO",
                            icon=ft.Icons.MOVING,
                            style=ft.ButtonStyle(
                                bgcolor = ft.Colors.DEEP_PURPLE_500,
                            ),
                            on_click=acessar_kanban
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


def apagar_kanban(e):
    # linha1 = e.control.parent -> acessa a ft.Row que contem o botão
    # coluna = linha.parent -> acessa a ft.Column que contem a ft.Row
    # container = coluna.parent -> acessa a ft.Container que contem a ft.Column
    # linha2 = container.parent -> acessa a ft.Row (mais externa) que contem o ft.Container
    # conteudo_da_linha = linha.parent -> acessa o conteudo da ft.Row mais externa
    container = e.control.parent.parent.parent
    conteudo_da_linha = container.parent.controls

    # pega o indice do kanban tanto do conteudo da linha quanto do banco de dados
    indice = conteudo_da_linha.index(container)
    
    # remove o kanban do banco de dados
    bd.pop(indice)

    # atualiza as rotas e atualiza a pagina
    con.carregar_rotas()


def acessar_kanban(e):
    # linha1 = e.control.parent -> acessa a ft.Row que contem o botão
    # coluna = e.control.parent.parent -> acessa a ft.Column que contem o botão
    # container = coluna.parent -> acessa a ft.Container que contem a ft.Column
    # linha2 = container.parent -> acessa a ft.Row (mais externa) que contem o ft.Container
    # conteudo_da_linha = linha.parent -> acessa o conteudo da ft.Row mais externa
    container = e.control.parent.parent.parent
    conteudo_da_linha = container.parent.controls

    # indice é somado com 2 para pular as rotas fixas 
    indice = conteudo_da_linha.index(container) + 2

    # acessa a pagina do kanban selecionado
    con.page.go(str(indice))
    # atualiza o navigation rail
    con.navigation_rail.selected_index = indice
    con.page.update()


def editar_kanban(e):
    pass


