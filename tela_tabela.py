import flet as ft
import controle as con
import tela_cadastro as tela
def view():     
    return ft.View(
                "tela1",
                controls =[           ft.AppBar(
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
                            con.rail,
                            ft.VerticalDivider(width=1),
                            ft.Column([ft.Stack([
                        ft.Container(
                            image_src='https://4kwallpapers.com/images/wallpapers/windows-11-stock-purple-abstract-black-background-amoled-2880x1800-9056.jpg',
                            image_fit=ft.ImageFit.COVER,
                            expand=True,
                            width=1980,
                            height=1080
                        ),ft.Text("MEMBROS"),ft.Row(scroll=ft.ScrollMode.ALWAYS,
                                                    #função da lista de membros vai aqui
                                                    controls =[ft.Container(   width=250,
                            height=250,
                                               bgcolor=ft.Colors.PURPLE,
                                padding = 20,   border=ft.border.all(2, ft.Colors.DEEP_PURPLE_500),
                         border_radius=10,content=ft.Column([ft.TextField("Pedro", bgcolor=ft.Colors.DEEP_PURPLE_500,
                                                                         read_only = True,  label = "Menbro",icon=ft.Icons.PERSON_2,label_style = ft.TextStyle(color = ft.Colors.WHITE,size = 15, italic=True  ),  text_style=        ft.TextStyle(color=ft.Colors.WHITE,
                                                                                         size=12,
                                                                             ) ),   ft.TextField("deve o agiota",label = "Atividades",label_style = ft.TextStyle(color = ft.Colors.WHITE,size = 15, italic=True  ),multiline = True,icon=ft.Icons.LIST_ALT_ROUNDED, bgcolor = ft.Colors.DEEP_PURPLE_500 )])) ])]) ], alignment=ft.MainAxisAlignment.START, expand=True),
                        ],
                        expand=True,
                    ),
            

            ] ,                  
                 

            )
