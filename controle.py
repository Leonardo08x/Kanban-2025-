import gerenciamento, filtrar, criacao, erro, visualizar
import flet as ft
import banco_de_dados

# variaveis globais
bd = []
rotas = {}
page = None
tela_atual = None
navigation_rail = None


def init(p):
    global page, bd
    page = p
    bd = banco_de_dados.carregar()

    carregar_rotas()


def controle_de_rota(rota):
    # apaga o conteudo da tela
    tela_atual.controls.clear()
    if rota.route in rotas.keys():
        # adiciona o conteudo da rota a tela
        tela_atual.controls += rotas[rota.route]
    else:
        # adiciona o conteudo da rota gerenciamento em caso de erro
        tela_atual.controls += erro.conteudo()

    # atualiza o navigation rail
    navigation_rail.selected_index = int(rota.route) if rota.route in rotas else 0
    
    page.update()


def carregar_rotas():
    # carrega as rotas pre-existentes (gerenciamento e membros) e as rotas dinamicas do bd
    global rotas, navigation_rail
    rotas = {
        '0': gerenciamento.conteudo(),
        '1': filtrar.conteudo(),
    }
    for i in range(len(bd)):
        rotas[str(i+2)] = visualizar.visualizar_kanban(i)

    banco_de_dados.salvar(bd)

    # atualiza o navigation rail com os campos fixos e os kanbans
    navigation_rail.destinations = destinos_navigation_rail()
    # atualiza a pagina
    controle_de_rota(page)


def atualizar_pagina(conteudo : list):
    global rotas
    rotas[page.route] = conteudo
    controle_de_rota(page)

# destinos do navigation rail
def destinos_navigation_rail():
    global bd
    destinos_fixos = [
            ft.NavigationRailDestination(
                icon=ft.Icons.LIST,
                selected_icon=ft.Icons.LIST_OUTLINED,
                label="INICIO"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.PERSON,
                selected_icon=ft.Icons.PERSON_OUTLINED,
                label="FILTROS"
            ),
        ]
    destinos_dinamicos = [
            ft.NavigationRailDestination(
                icon=ft.Icons.TASK_ALT,
                selected_icon=ft.Icons.TASK_ALT_OUTLINED,
                label=nome_do_kanban
            )
            for nome_do_kanban in [kanban.get('nome') for kanban in bd]
        ]
    return destinos_fixos + destinos_dinamicos 


# tela atual que vai adiquirir o conteudo das rotas
tela_atual = ft.Row(expand=True)


# appbar padronizada
appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.TASK_ALT),
        leading_width=100,
        center_title=False,
        toolbar_height=55,
        bgcolor=ft.Colors.PURPLE_300,
        title=ft.Text(
                        text_align=ft.TextAlign.START,
                        spans=[
                            ft.TextSpan(
                                "KANBAN",
                                ft.TextStyle(
                                    size=32,
                                    font_family="Kanit",
                                    weight=ft.FontWeight.BOLD,
                                    foreground=ft.Paint(
                                        gradient=ft.PaintLinearGradient(
                                            (2000, 150),
                                            (150, 2000),
                                            [ft.Colors.BLACK, ft.Colors.PURPLE]
                                        )
                                    ),
                                ),
                            ),
                        ],
                    )

    )



# navigation rail que fica na esquerda da tela e contem os icones das rotas
navigation_rail = ft.NavigationRail(
    label_type=ft.NavigationRailLabelType.ALL,
    group_alignment=-1.0,
    min_width=100,
    min_extended_width=400,
    bgcolor=ft.Colors.PURPLE_500,
    leading = ft.FloatingActionButton(
        icon=ft.Icons.ADD_TASK,
        text="Add",
        on_click = lambda e: page.open(criacao.alerta_dialog)
    ),
    destinations = destinos_navigation_rail(),
    on_change = lambda e: page.go(str(e.control.selected_index))
)


# view atual
view_atual = ft.Row(
    controls=[
        navigation_rail,
        ft.Stack(
            controls=[
                ft.Container(
                    image_src='https://4kwallpapers.com/images/wallpapers/windows-11-stock-purple-abstract-black-background-amoled-2880x1800-9056.jpg',
                    image_fit=ft.ImageFit.COVER,
                    expand=True,
                    width=1980,
                    height=1080
                ),
                tela_atual,
            ]
        )
    ],
    expand=True
)

