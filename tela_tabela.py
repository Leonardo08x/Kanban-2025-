import flet as ft
import controle as con

def view():
    return ft.View(
        "tela1",
        controls = [
            ft.AppBar(
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
            ),
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
                                    ft.Text("MEMBROS"),
                                    ft.Row(
                                        scroll=ft.ScrollMode.ALWAYS,
                                        #função da lista de membros vai aqui
                                        controls = con.recuperar_membros()
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
