import flet as ft
import controle as con


def main(page: ft.Page):
    con.init(page)
    page.window.width = 1920
    page.window.height = 1080
    page.window.maximized = True
    page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.DEEP_PURPLE)
    page.appbar = con.appbar
    
    
    page.on_route_change = con.controle_de_rota
    page.route = "0"

    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Open Sans": "fonts/OpenSans-Regular.ttf",
    }
    page.add(con.view_atual)


ft.app(target=main)



# TODO - pesquisa para caixa de selacao