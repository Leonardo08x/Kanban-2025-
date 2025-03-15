from time import sleep

import flet as ft
import controle as con

def main(page: ft.Page):

    con.init(page)
    page.on_route_change = con.controle_de_rota
    page.window.width = 1920
    page.window.height = 1080
    #titulo do exe
    page.title = "Sistema de cadastro"
    #controle de rota
    
    #tema
    page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.DEEP_PURPLE)

    #pagina inicial
    page.go('0')
    #puxa as fontes daqui
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Open Sans": "fonts/OpenSans-Regular.ttf",
    }


ft.app(target=main)