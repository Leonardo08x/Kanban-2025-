
import flet as ft
import controle as con

def main(page: ft.Page):   
    con.init(page)         
    page.title = "Sistema de cadastro"           
    page.on_route_change = con.controle_de_rota  
    page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.DEEP_PURPLE)
    page.go('1')
    #puxa as fontes daqui
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Open Sans": "fonts/OpenSans-Regular.ttf",
    }



ft.app(target=main)

