import flet as ft
import controle as con
import funcoes as fun
import criacao as cri


def view(limite, cores, nome_do_Kanbam):
    return ft.View(
        "tela2",
        controls =[
            ft.AppBar(
                leading=ft.Icon(ft.Icons.TASK_ALT),
                leading_width=100,
                actions=[
                    #botão salvar
                    ft.IconButton(
                        ft.Icons.SAVE,
                        icon_color=ft.Colors.WHITE,
                        icon_size=30,
                        on_click=lambda e: print("teste salvar")    #adicionar funcao
                    ),
                    #botão apagar adicionar função
                    ft.IconButton(
                        icon=ft.Icons.DELETE_FOREVER_ROUNDED,
                        icon_color=ft.Colors.WHITE,
                        icon_size=30,
                        on_click=fun.deletar_kanbam
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
            ), # AppBar
            ft.Row(
                [
                    ft.NavigationRail(
                        selected_index=None,
                        label_type=ft.NavigationRailLabelType.ALL,
                        bgcolor=ft.Colors.PURPLE_500,
                        min_width=100,
                        min_extended_width=400,
                        leading=ft.FloatingActionButton(
                            icon=ft.Icons.ADD_TASK,
                            text="Add",
                            on_click = lambda e: con.page.open(cri.painel_de_criacao)
                        ),
                        group_alignment=-0.9,
                        on_change= lambda e:  con.page.go(str(e.control.selected_index)),
                        destinations = con.destinos
                    ),
                    ft.VerticalDivider(width=1),
                    ft.Column(
                        scroll=ft.ScrollMode.ALWAYS,
                        controls = [
                            ft.Stack(
                                [
                                    ft.Container(
                                        image_src='https://4kwallpapers.com/images/wallpapers/windows-11-stock-purple-abstract-black-background-amoled-2880x1800-9056.jpg',
                                        image_fit=ft.ImageFit.COVER,
                                        expand=True,
                                        width=1980,
                                        height=1080
                                    ),
                                    ft.Text(nome_do_Kanbam),
                                    ft.Column(
                                        scroll=ft.ScrollMode.ADAPTIVE,
                                        controls=[
                                            ft.Row(
                                               scroll=ft.ScrollMode.ALWAYS,
                                               controls=con.recuperar_colunas(limite, cores)
                                            ) # Row
                                        ]
                                    ) # Column
                                ]
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        expand=True
                    ) # Column
                ],
                expand=True,
            ) # Row
        ]
    )