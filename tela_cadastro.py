import flet as ft
import controle as con


def view():
    return ft.View(
        "tela0",
        controls =[
            #appbar titulo
            ft.AppBar(
                leading=ft.Icon(ft.Icons.TASK_ALT),
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
                                        [
                                            ft.Colors.BLACK,
                                            ft.Colors.PURPLE
                                        ]
                                    )
                                ),
                            ),
                        ),
                    ]
                )
            ),
            # primeira linha
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
                                    ft.Column(
                                        [
                                            # Segunda linha, pesquisa, programar a pesquisa
                                            ft.Column(
                                                [
                                                    ft.Row(
                                                    [
                                                        ft.TextField(
                                                                label='pesquisar',
                                                                label_style =  ft.TextStyle(font_family="Kanit"),
                                                                icon='search',
                                                                on_change=lambda e: print("EU QUERO GOZARRRR"),
                                                                bgcolor= ft.Colors.PURPLE_500
                                                            ),ft.Checkbox(label="PESQUISAR POR ATIVIDADE", on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.DEEP_PURPLE,shape= ft.CircleBorder())
                                                           , ft.Checkbox(label="PESQUISAR POR USUARIO", on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.DEEP_PURPLE,shape= ft.CircleBorder())
                                                        ]
                                                    ), # Row
                                                    ft.Row(
                                                        scroll=ft.ScrollMode.ALWAYS,
                                                        controls = con.recuperar_kanbam()
                                                    ) # Row
                                                ]
                                            ),
                                            # botão adicionar, incluir em uma linha
                                            ft.FloatingActionButton(
                                                icon=ft.Icons.ADD,
                                                on_click=lambda e: con.page.open(con.painel_de_criacao),
                                                bgcolor=ft.Colors.PURPLE
                                            ),
                                            #incluir aqui a função dos kanbans
                                        ]
                                    ) # Column
                                ]
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        expand=True
                    ) # Column
                ],
                expand=True
            ) # Row
        ]
    )
