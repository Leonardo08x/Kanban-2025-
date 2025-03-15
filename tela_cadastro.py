import flet as ft
import controle as con
import criacao as cri


def view():
    return ft.View(
        "tela0",
        controls =[
            #appbar titulo
            con.appbar,
            # primeira linha
            ft.Row(
                expand=True,
                controls= [
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
                tight=True
            ) # Row
        ]
    )
