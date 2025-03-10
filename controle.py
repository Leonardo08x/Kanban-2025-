import tela_cadastro, tela_tabela
import flet as ft
#TROCAR PAGINA PELO ON CLICK NA INICIAL
#
componentes = {
        'cor_teste': ft.Ref[ft.Checkbox](),
        #add todos os compontens da tela aqui
    }

def init(p):
    global page, telas
#funão de adicionar views linkada ao navigation rail
    page = p
    telas = {
        '0': tela_cadastro.view(),
        '1': tela_tabela.view(),
        '2': ft.View(
                "tela2",
                controls =[           ft.AppBar(
                leading=ft.Icon(ft.Icons.TASK_ALT),
                leading_width=100,
                actions=[
                    #botão salvar, adicionar função
                        ft.IconButton(ft.Icons.SAVE, icon_color=ft.Colors.WHITE,
                        icon_size=30,on_click=lambda e: print("teste gay")),
                   #botão apagar adicionar função
                    ft.IconButton(
                        icon=ft.Icons.DELETE_FOREVER_ROUNDED,
                        icon_color=ft.Colors.WHITE,
                        icon_size=30,)
                    ],
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
                            rail,
                            ft.VerticalDivider(width=1),
                            ft.Column([ft.Stack([
                        ft.Container(
                            image_src='https://4kwallpapers.com/images/wallpapers/windows-11-stock-purple-abstract-black-background-amoled-2880x1800-9056.jpg',
                            image_fit=ft.ImageFit.COVER,
                            expand=True,
                            width=1980,
                            height=1080
                        ),ft.Text("TESTE"), ft.Column([ft.Row(
                                    #função de listas vai aqui
            [
                #main container
               ft.Container( width=250,
                        margin=60,
                        height=250,
                            border=ft.border.all(2, ft.Colors.PURPLE),
                         border_radius=10,
                              padding = 10,
                        bgcolor=ft.Colors.ORANGE_400,content=ft.DragTarget(
                    on_accept=drag_accept,
                    content=ft.Draggable(ft.Column(controls =[ft.TextField("", bgcolor=ft.Colors.WHITE,
                                                                           label = "[Atividadde]:",label_style = ft.TextStyle(color = ft.Colors.BLACK,size = 15, italic=True  ),  text_style=        ft.TextStyle(color=ft.Colors.BLACK,
                                                                                         size=12,
                                                                             ) ),ft.TextField("", bgcolor=ft.Colors.WHITE,
                                                                           label = "[Responsavel]:", icon= ft.Icon(name=ft.Icons.ARROW_CIRCLE_RIGHT, color=ft.Colors.WHITE,size=30,tooltip="mover"),label_style = ft.TextStyle(color = ft.Colors.BLACK,size = 12, italic=True  ),  text_style=        ft.TextStyle(color=ft.Colors.BLACK,
                                                                                         size=12,
                                                                             ) ),ft.TextField("",label= "[Descrição]:",label_style = ft.TextStyle(color = ft.Colors.BLACK, size = 15,italic=True ),multiline=True, bgcolor=ft.Colors.WHITE,
                                                                             text_style=        ft.TextStyle(color=ft.Colors.BLACK,
                                                                                         size=12
                                                                             ))])),
                ),),
                #main container
                ft.Container(width=250,
                             margin=60,
                             height=250,
                             border=ft.border.all(2, ft.Colors.PURPLE),
                             border_radius=10,
                             padding=10,
                             bgcolor=ft.Colors.ORANGE_400, content=ft.DragTarget(
                        on_accept=drag_accept,
                        content=ft.Draggable(ft.Column(controls =[ft.TextField("", bgcolor=ft.Colors.WHITE,
                                                                     label="[Atividadde]:",
                                                                     label_style=ft.TextStyle(color=ft.Colors.BLACK,
                                                                                              size=15, italic=True),
                                                                     text_style=ft.TextStyle(color=ft.Colors.BLACK,
                                                                                             size=12,
                                                                                             )),
                                                                                                              ft.TextField(
                                                                                                                  "",
                                                                                                                  bgcolor=ft.Colors.WHITE,
                                                                                                                  label="[Responsavel]:",
                                                                                                                  icon= ft.Icon(name=ft.Icons.ARROW_CIRCLE_RIGHT, color=ft.Colors.WHITE,size=30,tooltip="mover"),

                                                                                                                  label_style=ft.TextStyle(
                                                                                                                      color=ft.Colors.BLACK,
                                                                                                                      size=12,
                                                                                                                      italic=True),
                                                                                                                  text_style=ft.TextStyle(
                                                                                                                      color=ft.Colors.BLACK,
                                                                                                                      size=12,
                                                                                                                      )),
                                                        ft.TextField("", label="[Descrição]:",
                                                                     label_style=ft.TextStyle(color=ft.Colors.BLACK,
                                                                                              size=15, italic=True),
                                                                     multiline=True, bgcolor=ft.Colors.WHITE,
                                                                     text_style=ft.TextStyle(color=ft.Colors.BLACK,
                                                                                             size=12
                                                                                             ))])),
                    ), ),  ft.FloatingActionButton(icon=ft.Icons.ADD,tooltip="adicionar cartão na linha", on_click=lambda e: page.open(painel_de_criacao2), bgcolor=ft.Colors.PURPLE)
            ]
        ),   ft.FloatingActionButton(icon=ft.Icons.ADD, tooltip="adicionar cartão na coluna",on_click=lambda e: page.open(painel_de_criacao2), bgcolor=ft.Colors.PURPLE)])]) ], alignment=ft.MainAxisAlignment.START, expand=True),
                        ],
                        expand=True,
                    )


            ] ,


            )
    }


def controle_de_rota(route_event):
    page.views.clear()
    page.views.append(telas[route_event.route])
    page.update()

def drag_accept(e):
        # get draggable (source) control by its ID
        src = page.get_control(e.src_id)
        print(src.content.controls)
        valor_inicial =  e.control.content.content.controls
        e.control.content.content.controls= src.content.controls
        src.content.controls = valor_inicial


        page.update()


# navegação
rail = ft.NavigationRail(

    selected_index=None,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        bgcolor=ft.Colors.PURPLE_500,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.Icons.ADD_TASK, text="Add",on_click= lambda e: page.open(painel_de_criacao)),
        group_alignment=-0.9,

        on_change= lambda e:  page.go(str(e.control.selected_index)),
        #função de destinos
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.LIST, selected_icon=ft.Icons.LIST_OUTLINED, label="INICIO"

            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.PERSON,
                selected_icon=ft.Icons.PERSON_OUTLINED,label="MEMBROS"),
            #TESTE
            ft.NavigationRailDestination(
                icon=ft.Icons.TASK_ALT,
                selected_icon=ft.Icons.TASK_ALT_OUTLINED, label="KANBAN TEMPLATE"),


        ])

def handle_close(e):
    page.close(painel_de_criacao)
    page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))
def handle_close2(e):
    page.close(painel_de_criacao2)
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
                    ft.Checkbox(label="",  ref=componentes['cor_teste'],on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.BLUE,shape= ft.CircleBorder())
                       ,]),

            ft.Row([ft.Text("Selecione o numero de colunas:")
                ,ft.RangeSlider(
        min=2,
        max=4,
        start_value=0,
        divisions=2,
        end_value=4,
        inactive_color=ft.Colors.GREY_900,
        active_color=ft.Colors.BLACK38,
        overlay_color=ft.Colors.BLACK,
        label="{value}",
    )]),
          ft.Row([
            #programar a função criar
            ft.TextButton("criar",style = ft.ButtonStyle(bgcolor = ft.Colors.BLACK38),  on_click=lambda e: print(componentes['cor_teste'].current.value)),
            ft.TextButton("cancelar", style = ft.ButtonStyle(bgcolor = ft.Colors.BLACK38),on_click=handle_close),
       ]),
       ],
        #style = ft.ButtonStyle(bgcolor = ft.Colors.PURPLE)
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(
            ft.Text("reali é gay"),
        ),
    )

painel_de_criacao2 = ft.AlertDialog(
        modal=True,
        bgcolor = ft.Colors.PURPLE,
        title=ft.Text("BUFAS EXE"),
        #color=ft.Colors.PURPLE
        content=ft.Text("escolha a cor do cartão"),

        actions=[

            ft.Row([ft.Checkbox(label="", on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.GREEN,shape= ft.CircleBorder()),
                    ft.Checkbox(label="", on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.RED,shape= ft.CircleBorder()),
                    ft.Checkbox(label="", on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.WHITE,shape= ft.CircleBorder()),
                    ft.Checkbox(label="", on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.BLACK,shape= ft.CircleBorder()),
                    ft.Checkbox(label="", on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.YELLOW,shape= ft.CircleBorder()),
                    ft.Checkbox(label="", on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.ORANGE,shape= ft.CircleBorder()),
                    ft.Checkbox(label="",  ref=componentes['cor_teste'],on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.BLUE,shape= ft.CircleBorder())
                       ,]),


          ft.Row([
            #programar a função criar
            ft.TextButton("criar",style = ft.ButtonStyle(bgcolor = ft.Colors.BLACK38),  on_click=lambda e: print(componentes['cor_teste'].current.value)),
            ft.TextButton("cancelar", style = ft.ButtonStyle(bgcolor = ft.Colors.BLACK38),on_click=handle_close2),
       ]),
       ],
        #style = ft.ButtonStyle(bgcolor = ft.Colors.PURPLE)
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(
            ft.Text("reali é gay"),
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
