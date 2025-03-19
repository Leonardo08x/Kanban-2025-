import gerenciamento, pesquisar, criacao, bd, erro, visualizar
import flet as ft


def init(p):
    global page
    page = p
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
    page.update()
    # atualiza o navigation rail
    navigation_rail.selected_index = int(rota.route) if rota.route in rotas else None


def carregar_rotas():
    # carrega as rotas pre-existentes (gerenciamento e membros) e as rotas dinamicas do bd
    global rotas, navigation_rail, destinos_fixos
    rotas = {
        '0': gerenciamento.conteudo(),
        '1': pesquisar.conteudo(),
    }
    for i, kanban in enumerate(bd.bd):
        rotas[str(i+2)] = visualizar.visualizar_kanban(i)

    # atualiza o navigation rail com os campos fixos e os kanbans
    navigation_rail.destinations = destinos_fixos + destinos_dinamicos()
    # atualiza a pagina
    controle_de_rota(page)


# variaveis globais #

# tela atual que vai adiquirir o conteudo das rotas
tela_atual = ft.Row(expand=True)


# appbar padronizada
appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.TASK_ALT),
        leading_width=100,
        center_title=False,
        toolbar_height=55,
        bgcolor=ft.Colors.PURPLE_300,
        title=ft.Text('Trolla'),
    )

# destinos do navigation rail
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
def destinos_dinamicos():
    return [
        ft.NavigationRailDestination(
            icon=ft.Icons.TASK_ALT,
            selected_icon=ft.Icons.TASK_ALT_OUTLINED,
            label=nome_do_kanban
        )
        for nome_do_kanban in [kanban.get('nome') for kanban in bd.bd]
    ]


# navigation rail que fica na esquerda da tela e contem os icones das rotas
navigation_rail = ft.NavigationRail(
    selected_index=0,
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
    destinations = destinos_fixos + destinos_dinamicos(),
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

