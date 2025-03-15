from time import sleep

import flet as ft
import controle as con

def main(page: ft.Page):
    con.init(page)
    page.on_route_change = con.controle_de_rota
    page.window.maximized = True    #abrir maximizado
    page.title = "Sistema de cadastro"  #titulo do exe
    page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.DEEP_PURPLE) #tema
    page.go('0')    #pagina inicial
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Open Sans": "fonts/OpenSans-Regular.ttf",
    }    #puxa as fontes daqui

ft.app(target=main)