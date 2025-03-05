import flet as ft
import controle as con



def view():

    return ft.View(


                "tela1",[
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
            ft.Row(
                [
                    con.barra_navegacao(),
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

                      #primeira linha

        #Segunda linha, teste de inserção
                        ft.Row(
                        [ ft.TextField(label='pesquisar',label_style =  ft.TextStyle(font_family="Kanit",), icon='search',
                                 on_change=lambda e: print("EU QUERO GOZARRRR"),bgcolor= ft.Colors.PURPLE_500)]#linha
                        ,
                        ),
                        ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=lambda e: con.page.open(con.painel_de_criacao), bgcolor=ft.Colors.PURPLE),



                    ]
                )])], alignment=ft.MainAxisAlignment.START, expand=True),
                ],
                expand=True,
            )
        ,]

    )
