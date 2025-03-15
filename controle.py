import tela_cadastro, tela_tabela, tela_teste, cor
import funcoes as fun
import flet as ft

#TROCAR PAGINA PELO ON CLICK NA INICIAL


########################criação de kanban##################################################################

def recuperar_colunas(limite, cores):
    colunas = []
    print(cores)
    for i in range(limite):
    #função de listas vai aqui
        colunas.append(
            # main container
            ft.Container(
                width=250,
                margin=60,
                height=250,
                border=ft.border.all(2, ft.Colors.PURPLE),
                border_radius=10,
                padding=10,
                on_long_press=expandir_coluna,
                bgcolor=cores[i],
                content=ft.Column(
                    controls=[
                        ft.DragTarget(
                            on_accept=drag_accept,
                            content=ft.Draggable(
                                ft.Column(
                                    controls = [
                                        ft.TextField(
                                            bgcolor = ft.Colors.WHITE,
                                            label = "[Atividadde]:",
                                            label_style = ft.TextStyle(
                                                color = ft.Colors.BLACK,
                                                size = 15,
                                                italic = True
                                            ),
                                            text_style = ft.TextStyle(
                                                color = ft.Colors.BLACK,
                                                size = 12
                                            )
                                        ), # TextField
                                        ft.TextField(
                                            bgcolor = ft.Colors.WHITE,
                                            label = "[Responsavel]:",
                                            icon = ft.Icon(
                                                name = ft.Icons.ARROW_CIRCLE_RIGHT,
                                                color = ft.Colors.WHITE,
                                                size = 30,
                                                tooltip = "mover"
                                            ),
                                            label_style = ft.TextStyle(
                                                color = ft.Colors.BLACK,
                                                size = 12,
                                                italic=True
                                            ),
                                            text_style = ft.TextStyle(
                                                color = ft.Colors.BLACK,
                                                size=12
                                                )
                                        ), # TextField
                                        ft.TextField(
                                            label = "[Descrição]:",
                                            label_style = ft.TextStyle(
                                                color = ft.Colors.BLACK,
                                                size = 15,
                                                italic=True
                                            ),
                                            multiline = True,
                                            bgcolor = ft.Colors.WHITE,
                                            text_style = ft.TextStyle(
                                                color=ft.Colors.BLACK,
                                                size=12
                                            )
                                        ) # TextField
                                    ]
                                )
                            )
                        ),
                        ft.Icon(
                           name=ft.Icons.ADD,
                           color=ft.Colors.WHITE,
                           size=30,
                           tooltip="segure para adicionar uma nova atividade\nmáximo de 4 ativiaddes"
                        )
                    ]
                )
            )
        )
    return colunas
##############################fim da criação###################################################################

##################################componentes##########################

appbar = ft.AppBar(
    leading=ft.Icon(ft.Icons.TASK_ALT),
    leading_width=100,
    center_title=False,
    toolbar_height=55,
    bgcolor=ft.Colors.PURPLE_300,
    title = ft.Text(
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
                            [
                                ft.Colors.BLACK,
                                ft.Colors.PURPLE
                            ]
                        )
                    )
                )
            )
        ]
    )
)

##############################fim dos componentes############################################


##########################listas##############################################################################

destinos = [
    ft.NavigationRailDestination(
        icon=ft.Icons.LIST,
        selected_icon=ft.Icons.LIST_OUTLINED,
        label="INICIO"
    ),
    ft.NavigationRailDestination(
        icon=ft.Icons.PERSON,
        selected_icon=ft.Icons.PERSON_OUTLINED,
        label="MEMBROS"
    ),
]


membros = [
    ft.Container(
        width=250,
        height=250,
        bgcolor=ft.Colors.PURPLE,
        padding = 20,
        border=ft.border.all(2, ft.Colors.DEEP_PURPLE_500),
        border_radius=10,
        content=ft.Column(
            [
                ft.TextField(
                    "Pedro",
                    bgcolor=ft.Colors.DEEP_PURPLE_500,
                    read_only = True,
                    label = "Menbro",
                    icon=ft.Icons.PERSON_2,
                    label_style = ft.TextStyle(
                        color = ft.Colors.WHITE,
                        size = 15,
                        italic=True
                    ),
                    text_style = ft.TextStyle(
                        color=ft.Colors.WHITE,
                        size=12,
                    )
                ), # TextField
                ft.TextField(
                    "deve o agiota",
                    label = "Atividades",
                    label_style = ft.TextStyle(
                        color = ft.Colors.WHITE,
                        size = 15,
                        italic=True
                    ),
                    multiline = True,
                    icon=ft.Icons.LIST_ALT_ROUNDED,
                    bgcolor = ft.Colors.DEEP_PURPLE_500
                ) # TextField
            ]
        ) # Column
    ) # Container
]


###########################################################fim das listas###################################


def init(p):
    global page, telas
    page = p
    telas = {
        '0': tela_cadastro.view(),
        '1': tela_tabela.view(),
    }


def controle_de_rota(route_event):
    global tela_atual
    page.views.clear()
    tela_atual = route_event.route
    page.views.append(telas[tela_atual])
    page.update()


def drag_accept(e):
    # get draggable (source) control by its ID
    src = page.get_control(e.src_id)
    valor_inicial = e.control.content.content.controls
    e.control.content.content.controls = src.content.controls
    src.content.controls = valor_inicial
    page.update()


#########################################utilidades#########################################################


def expandir_coluna(e):
    if len(e.control.content.controls) < 7:
        e.control.height+=195
        e.control.content.controls.extend(
            [
                ft.Divider(
                    height=5,
                    color="white"
                ),                      
                ft.DragTarget(
                    on_accept=drag_accept,
                    content=ft.Draggable(
                        ft.Column( 
                            controls = [
                                ft.TextField(
                                    bgcolor = ft.Colors.WHITE,
                                    label = "[Atividadde]:",
                                    label_style = ft.TextStyle(
                                        color = ft.Colors.BLACK,
                                        size = 15,
                                        italic = True
                                    ),
                                    text_style = ft.TextStyle(
                                        color = ft.Colors.BLACK,
                                        size = 12,
                                    )
                                ),
                                ft.TextField(
                                    bgcolor = ft.Colors.WHITE,
                                    label = "[Responsavel]:",
                                    icon = ft.Icon(
                                        name = ft.Icons.ARROW_CIRCLE_RIGHT,
                                        color = ft.Colors.WHITE,
                                        size = 30,
                                        tooltip = "mover"
                                    ),
                                    label_style = ft.TextStyle(
                                        color = ft.Colors.BLACK,
                                        size = 12,
                                        italic=True
                                    ),
                                    text_style = ft.TextStyle(
                                        color = ft.Colors.BLACK,
                                        size=12
                                        )
                                ),
                                ft.TextField(
                                    label = "[Descrição]:",
                                    label_style = ft.TextStyle(
                                        color = ft.Colors.BLACK,
                                        size = 15,
                                        italic=True
                                    ),
                                    multiline = True,
                                    bgcolor = ft.Colors.WHITE,
                                    text_style = ft.TextStyle(
                                        color=ft.Colors.BLACK,
                                        size=12
                                    )
                                )
                            ]
                        )
                    )
                )   
            ]
        )
    page.update()


#########################################################fim de utilidades#####################################
