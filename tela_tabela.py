import flet as ft
import controle as con
import criacao as cri

def view():
    return ft.View(
        "tela1",
        controls = [
            con.appbar,
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
                                    ft.Text("MEMBROS"),
                                    ft.Row(
                                        scroll=ft.ScrollMode.ALWAYS,
                                        #função da lista de membros vai aqui
                                        controls = con.membros
                                    ) # Row
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
