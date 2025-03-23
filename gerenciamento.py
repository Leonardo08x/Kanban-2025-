import flet as ft
from flet.core.icons import icons

import controle as con
import banco_de_dados


# TODO alterar visualização, deixar a linha de cartões formando colunas, semelhante a ResponsiveRow

def conteudo() -> list:
    return [
        ft.Column(
            controls=[
                ft.Text(
                    value='✒ TELA DE GERENCIAMENTO ✒',
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
                    ),
                ),
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
                                criar_cartao_do_kanban(kanban.get('nome'))
                                for kanban in con.bd
                            ]
                        )
                    ]
                )
            ],
        )
    ]


# gera um cartão padronizado com todo o nome do kanban e os botões para acessá-lo, editá-lo e excluí-lo
def criar_cartao_do_kanban(nome_do_kanban : str) -> ft.Container:
    return ft.Container(
        alignment=ft.alignment.top_left,
        width=250,
        height=150,
        bgcolor=ft.Colors.PURPLE,
        padding=20,
        border=ft.border.all(2, ft.Colors.DEEP_PURPLE_500),
        border_radius=50,
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
                            icon=ft.Icons.DELETE,
                            style=ft.ButtonStyle(
                                bgcolor = ft.Colors.DEEP_PURPLE_500,
                            )
                        ),
                        # botão de acesso ao kanban
                        ft.ElevatedButton(
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


# função do botão apagar o kanban
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
    banco_de_dados.excluir(indice, con.bd)
    con.bd.pop(indice)
    
    # atualiza as rotas e atualiza a pagina
    con.carregar_rotas()


# função do botão de acesso ao kanban
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


# função do botão de editar
def editar_kanban(e):
    # TODO implementar funcao do botao para editar o kanban selecionado
    pass


