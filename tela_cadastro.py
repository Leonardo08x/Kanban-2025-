import flet as ft
from typing_extensions import ReadOnly

import controle as con


def view():

    return ft.View(

                "tela0",controls =[
            #appbar titulo
            ft.AppBar(
                leading=ft.Icon(ft.Icons.TASK_ALT),
                leading_width=100,
                title=ft.Text(
                    spans=[
                ft.TextSpan(
                    "KANBAN",
                    ft.TextStyle(
                        size=32,
                        font_family="Kanit",
                        weight=ft.FontWeight.BOLD,
                        foreground=ft.Paint(
                            gradient=ft.PaintLinearGradient(
                                (2000, 150), (150, 2000), [ft.Colors.BLACK, ft.Colors.PURPLE]
                            )
                        ),
                    ),
                ),
            ],

                    text_align=ft.TextAlign.START,
                ),
                center_title=False,
                toolbar_height=55,
                bgcolor=ft.Colors.PURPLE_300,
            ),
            # primeira linha
            ft.Row(
                [
                    con.rail,
                    ft.VerticalDivider(width=1),
                    ft.Column([ft.Stack([
                        ft.Container(
                            image_src='https://4kwallpapers.com/images/wallpapers/windows-11-stock-purple-abstract-black-background-amoled-2880x1800-9056.jpg',
                            image_fit=ft.ImageFit.COVER,
                            expand=True,
                            width=1980,
                            height=1080
                        )
,                        ft.Column(
                    [



        #Segunda linha, pesquisa, programar a pesquisa
                       ft.Column( [ft.Row(
                        [ ft.TextField(label='pesquisar',label_style =  ft.TextStyle(font_family="Kanit",), icon='search',
                                 on_change=lambda e: print("EU QUERO GOZARRRR"),bgcolor= ft.Colors.PURPLE_500)]#linha
                        ,
                        ),

                       ft.Row(scroll=ft.ScrollMode.ALWAYS,controls =
                       #função da lista de kanbans vai aqui
                       [ft.Container(   width=220,
                            height=150,
                                               bgcolor=ft.Colors.PURPLE,
                                padding = 20,   border=ft.border.all(2, ft.Colors.DEEP_PURPLE_500),
                         border_radius=10,content=ft.Column([ft.TextField("Kanban Template", bgcolor=ft.Colors.DEEP_PURPLE_500,
                                                                         read_only = True,  label = "Nome do Kanban",icon=ft.Icons.TASK_ALT,label_style = ft.TextStyle(color = ft.Colors.WHITE,size = 15, italic=True  ),  text_style=        ft.TextStyle(color=ft.Colors.WHITE,
                                                                                         size=12,




                                                                             ) ),
                    #funcao go linkada ao index do view
                    ft.TextButton("GO",icon=ft.Icons.MOVING, style = ft.ButtonStyle(bgcolor = ft.Colors.DEEP_PURPLE_500),on_click=lambda e: con.page.go('2') )])) ])]),
            #botão adicionar, incluir em uma linha
                        ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=lambda e: con.page.open(con.painel_de_criacao), bgcolor=ft.Colors.PURPLE),
            #incluir aqui a função dos kanbans


                    ]
                )])], alignment=ft.MainAxisAlignment.START, expand=True),
                ],
                expand=True,
            )
        ,]

    )
