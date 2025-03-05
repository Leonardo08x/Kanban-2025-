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
        #selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        bgcolor=ft.Colors.PURPLE_500,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.Icons.CREATE, text="Add",on_click= lambda e: page.open(painel_de_criacao)),
        group_alignment=-0.9,

        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.FAVORITE_BORDER, selected_icon=ft.Icons.FAVORITE, label="INICIO"

            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.BOOKMARK_BORDER,),
                selected_icon=ft.Icon(ft.Icons.BOOKMARK),label="MEMBROS"),
        ], on_change= lambda e: page.go(str(e.control.selected_index+1)),)
def handle_close(e):
    page.close(painel_de_criacao)
    page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))
painel_de_criacao = ft.AlertDialog(
        modal=True,
        bgcolor = ft.Colors.PURPLE,
        title=ft.Text("BUFAS EXE"),
        #color=ft.Colors.PURPLE
        #content=ft.Text("rato arabe passate a bufa, aceitas ?"),
        content=ft.TextField(label='nome do KANBAN',label_style =  ft.TextStyle(font_family="Kanit",), icon='TASK_ALT'),

        actions=[

            ft.Row([ft.Checkbox(label="", on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.GREEN,shape= ft.CircleBorder()),
                    ft.Checkbox(label="", on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.RED,shape= ft.CircleBorder()),
                    ft.Checkbox(label="", on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.WHITE,shape= ft.CircleBorder()),
                    ft.Checkbox(label="", on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.BLACK,shape= ft.CircleBorder()),
                    ft.Checkbox(label="", on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.YELLOW,shape= ft.CircleBorder()),
                    ft.Checkbox(label="", on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.ORANGE,shape= ft.CircleBorder()),
                    ft.Checkbox(label="", on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.BLUE,shape= ft.CircleBorder())
                       ,]),

            ft.Row([ft.Text("Selecione o numero de colunas:")
                ,ft.RangeSlider(
        min=0,
        max=4,
        start_value=0,
        divisions=4,
        end_value=4,
        inactive_color=ft.Colors.GREY_900,
        active_color=ft.Colors.BLACK38,
        overlay_color=ft.Colors.BLACK,
        label="{value}",
    )]),
          ft.Row([
            ft.TextButton("criar",style = ft.ButtonStyle(bgcolor = ft.Colors.BLACK38),  on_click=handle_close),
            ft.TextButton("cancelar", style = ft.ButtonStyle(bgcolor = ft.Colors.BLACK38),on_click=handle_close),
       ]),
       ],
        #style = ft.ButtonStyle(bgcolor = ft.Colors.PURPLE)
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(
            ft.Text("SEU INFIEL"),
        ),
    )



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
