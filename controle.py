import tela_cadastro, tela_tabela
import flet as ft

 


def init(p):
    global page, telas
    page = p
    telas = {
        '1': tela_cadastro.view(),
        '2': tela_tabela.view()
    }


def controle_de_rota(route_event):
    page.views.clear()    
    page.views.append(telas[route_event.route])    
    page.update()


#navegação
def barra_navegacao():
    return ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        bgcolor=ft.Colors.PURPLE_500,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.Icons.CREATE, text="Add"),
        group_alignment=-0.9,

        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.FAVORITE_BORDER, selected_icon=ft.Icons.FAVORITE, label="First"

            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.BOOKMARK_BORDER,),
                selected_icon=ft.Icon(ft.Icons.BOOKMARK),label="Second"),
        ], on_change= lambda e: page.go(str(e.control.selected_index+1)),)

    """, label_content=ft.TextField(
                           value="bct",
                           hint_text="bct",
                           text_size=12,
                           read_only=True,
                           #on_focus=self.board_name_focus,
                           #on_blur=self.board_name_blur,
                           #border=ft.InputBorder.NONE,
                           height=50,
                           width=150,
                           text_align=ft.TextAlign.START,
                           #data=i,
                       )"""





    """ft.NavigationBar(

        
       bgcolor = ft.Colors.DEEP_PURPLE_700,
        indicator_color = ft.Colors.PURPLE_800,

                        destinations=[
                            ft.NavigationBarDestination(icon=ft.icons.SAVE, label="Cadastrar",),
                            ft.NavigationBarDestination(icon=ft.icons.SEARCH, label="Listar"),                            
                        ],
                        
                       , on_change= lambda e: page.go(str(e.control.selected_index+1))
            )#NavigationBar"""
