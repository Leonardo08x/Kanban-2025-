import flet as ft
import controle as con


def main(page: ft.Page):
    con.init(page)
    
    page.title = "Trolla"
    page.window.maximized = True
    page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.DEEP_PURPLE)
    page.appbar = con.appbar
    
    
    page.on_route_change = con.controle_de_rota
    page.route = "0"


    page.add(con.view_atual)


ft.app(target=main)

