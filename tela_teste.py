import flet as ft
import controle as con

def view():
    return ft.View(
        "tela2",
        controls =[
            ft.AppBar(
                leading=ft.Icon(ft.Icons.TASK_ALT),
                leading_width=100,
                actions=[
                    #botão salvar, adicionar função
                    ft.IconButton(
                        ft.Icons.SAVE,
                        icon_color=ft.Colors.WHITE,
                        icon_size=30,
                        on_click=lambda e: print("salvamento efetuado"),
                    ),
                    #botão apagar adicionar função
                    ft.IconButton(
                        icon=ft.Icons.DELETE_FOREVER_ROUNDED,
                        icon_color=ft.Colors.WHITE,
                        icon_size=30,
                        on_click=lambda e: print("apagamento efetuado"),
                    )
                ],
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
                                        [
                                            ft.Colors.BLACK,
                                            ft.Colors.PURPLE
                                        ]
                                    )
                                )
                            )
                        )
                    ]
                ),
                center_title=False,
                toolbar_height=55,
                bgcolor=ft.Colors.PURPLE_300,
            ), # Appbar
            ft.Row(
                [
                    con.rail,
                    ft.VerticalDivider(width=1),
                    ft.Column(
                        [
                            ft.Stack(
                                [
                                    ft.Container(
                                        image_src='https://4kwallpapers.com/images/wallpapers/windows-11-stock-purple-abstract-black-background-amoled-2880x1800-9056.jpg',
                                        image_fit=ft.ImageFit.COVER,
                                        expand=True,
                                        width=1980,
                                        height=1080
                                    ),
                                    ft.Text("TESTE"),
                                    ft.Column(
                                        [
                                            ft.Row(
                                            #função de listas vai aqui
                                                [
                                                    # main container
                                                    ft.Container(
                                                        width=250,
                                                        margin=60,
                                                        height=250,
                                                        border=ft.border.all(2, ft.Colors.PURPLE),
                                                        border_radius = 10,
                                                        padding = 10,
                                                        bgcolor=ft.Colors.ORANGE_400,
                                                        content=ft.DragTarget(
                                                            on_accept=con.drag_accept,
                                                            content=ft.Draggable(
                                                                ft.Column(
                                                                    controls = [
                                                                        ft.TextField(
                                                                            "",
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
                                                                            "",
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
                                                                            "",
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
                                                            ),
                                                        )
                                                    ),
                                                    # main container
                                                    ft.Container(
                                                        width=250,
                                                        margin=60,
                                                        height=250,
                                                        border=ft.border.all(2, ft.Colors.PURPLE),
                                                        border_radius=10,
                                                        padding=10,
                                                        bgcolor=ft.Colors.ORANGE_400,
                                                        content=ft.DragTarget(
                                                            on_accept=con.drag_accept,
                                                            content=ft.Draggable(
                                                                ft.Column(
                                                                    controls = [
                                                                        ft.TextField(
                                                                            "",
                                                                            bgcolor=ft.Colors.WHITE,
                                                                            label = "[Atividadde]:",
                                                                            label_style = ft.TextStyle(
                                                                                color=ft.Colors.BLACK,
                                                                                size=15, italic=True
                                                                            ),
                                                                            text_style=ft.TextStyle(
                                                                                color=ft.Colors.BLACK,
                                                                                size=12,
                                                                            )
                                                                        ),
                                                                        ft.TextField(
                                                                            "",
                                                                            bgcolor=ft.Colors.WHITE,
                                                                            label="[Responsavel]:",
                                                                            icon= ft.Icon(
                                                                                name=ft.Icons.ARROW_CIRCLE_RIGHT,
                                                                                color=ft.Colors.WHITE,
                                                                                size=30,
                                                                                tooltip="mover"
                                                                            ),
                                                                            label_style=ft.TextStyle(
                                                                                color=ft.Colors.BLACK,
                                                                                size=12,
                                                                                italic=True
                                                                            ),
                                                                            text_style=ft.TextStyle(
                                                                                color=ft.Colors.BLACK,
                                                                                size=12,
                                                                                )
                                                                        ),
                                                                        ft.TextField(
                                                                            "",
                                                                            label="[Descrição]:",
                                                                            label_style=ft.TextStyle(
                                                                                color=ft.Colors.BLACK,
                                                                                size=15,
                                                                                italic=True
                                                                            ),
                                                                            multiline=True,
                                                                            bgcolor=ft.Colors.WHITE,
                                                                            text_style=ft.TextStyle(
                                                                                color=ft.Colors.BLACK,
                                                                                size=12
                                                                            )
                                                                        )
                                                                    ]
                                                                )
                                                            ),
                                                        ),
                                                    ),
                                                    ft.FloatingActionButton(
                                                        icon=ft.Icons.ADD,
                                                        tooltip="adicionar atividade",
                                                        on_click=lambda e: con.page.open(con.painel_de_criacao2),
                                                        bgcolor=ft.Colors.PURPLE
                                                    )
                                                ]
                                            ),
                                            ft.FloatingActionButton(
                                                icon=ft.Icons.ADD,
                                                tooltip="adicionar cartão na coluna",
                                                on_click=lambda e: con.page.open(con.painel_de_criacao2),
                                                bgcolor=ft.Colors.PURPLE
                                            )
                                        ]
                                    )
                                ]
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        expand=True
                    ),
                ],
                expand=True,
            ) # Row
        ]
    )