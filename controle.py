import tela_cadastro, tela_tabela
import flet as ft

#TROCAR PAGINA PELO ON CLICK NA INICIAL


########################criação de kanban##################################################################
def desabilita_botão_criar(e):
    cores = []
    nome_do_Kanbam = nome_kamb.value
    
    limite = int(slider.value)

    BLUE = blue.value
    if BLUE == True:
        cores.append(ft.Colors.BLUE)

    GRENN =  green.value
    if GRENN  == True:
        cores.append(ft.Colors.GREEN )

    RED = red.value
    if  RED== True:
        cores.append(ft.Colors.RED)

    YELLOW = yellow.value
    if YELLOW == True:
        cores.append(ft.Colors.YELLOW)

    ORANGE = orange.value
    if ORANGE == True:
        cores.append(ft.Colors.ORANGE)

    if len(list(telas.keys()))<10:

        if len(cores) == limite:
                    criar_botao.disabled = False
        else:
                criar_botao.disabled = True
    else:
                criar_botao.disabled = True
    page.update()
def recuperar_colunas(limite,cores):
    colunas = []
    print(cores)
    for i in range(limite):
    #função de listas vai aqui
        colunas.append(
            # main container
            ft.Container(
                width=250,
                margin=60,
                height=250,
                border=ft.border.all(2, ft.Colors.PURPLE),
                border_radius = 10,
                padding = 10,
                bgcolor=cores[i],
                content=ft.DragTarget(
                    on_accept=drag_accept,
                    content=ft.Draggable(
                        ft.Column(
                            controls = [
                                ft.TextField(
                                    "",
                                    bgcolor = ft.Colors.WHITE,
                                    label = "[Atividadde]:",
                                    label_style = ft.TextStyle(
                                        color = ft.Colors.BLACK,
                                        size = 15,
                                        italic = True
                                    ),
                                    text_style = ft.TextStyle(
                                        color = ft.Colors.BLACK,
                                        size = 12,
                                    )
                                ),
                                ft.TextField(
                                    "",
                                    bgcolor = ft.Colors.WHITE,
                                    label = "[Responsavel]:",
                                    icon = ft.Icon(
                                        name = ft.Icons.ARROW_CIRCLE_RIGHT,
                                        color = ft.Colors.WHITE,
                                        size = 30,
                                        tooltip = "mover"
                                    ),
                                    label_style = ft.TextStyle(
                                        color = ft.Colors.BLACK,
                                        size = 12,
                                        italic=True
                                    ),
                                    text_style = ft.TextStyle(
                                        color = ft.Colors.BLACK,
                                        size=12
                                        )
                                ),
                                ft.TextField(
                                    "",
                                    label = "[Descrição]:",
                                    label_style = ft.TextStyle(
                                        color = ft.Colors.BLACK,
                                        size = 15,
                                        italic=True
                                    ),
                                    multiline = True,
                                    bgcolor = ft.Colors.WHITE,
                                    text_style = ft.TextStyle(
                                        color=ft.Colors.BLACK,
                                        size=12
                                    )
                                )
                            ]
                        )
                    ),
                )
            )
        )
                            
    return colunas

def criar_kanban(e):
   cores = []
   nome_do_Kanbam = nome_kamb.value
   print(slider.value)
   limite = int(slider.value)

   BLUE = blue.value
   if BLUE == True:
    cores.append(ft.Colors.BLUE)

   GRENN =  green.value
   if GRENN  == True:
    cores.append(ft.Colors.GREEN )

   RED = red.value
   if  RED== True:
    cores.append(ft.Colors.RED)

   YELLOW = yellow.value
   if YELLOW == True:
    cores.append(ft.Colors.YELLOW)

   ORANGE = orange.value
   if ORANGE == True:
    cores.append(ft.Colors.ORANGE)
  
   template_view =  ft.View(
            "tela2",
            controls =[
                ft.AppBar(
                    leading=ft.Icon(ft.Icons.TASK_ALT),
                    leading_width=100,
                    actions=[
                        #botão salvar, adicionar função
                        ft.IconButton(
                            ft.Icons.SAVE,
                            icon_color=ft.Colors.WHITE,
                            icon_size=30,on_click=lambda e: print("teste gay")
                        ),
                        #botão apagar adicionar função
                        ft.IconButton(
                            icon=ft.Icons.DELETE_FOREVER_ROUNDED,
                            icon_color=ft.Colors.WHITE,
                            icon_size=30,on_click =deletar_kanbam)
                    ],
                    title=ft.Text(
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
                                            [ft.Colors.BLACK, ft.Colors.PURPLE]
                                        )
                                    ),
                                ),
                            ),
                        ],
                    ),
                    center_title=False,
                    toolbar_height=55,
                    bgcolor=ft.Colors.PURPLE_300,
                ),
                ft.Row(
                    [
                        rail,
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
                                        ft.Text(f"{nome_do_Kanbam}"),
                                        ft.Column([ft.Row( scroll=ft.ScrollMode.ALWAYS,controls=
                                  recuperar_colunas(limite,cores))])
                                    ]
                                )
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            expand=True
                        ),
                    ],
                    expand=True,
                ) # Row
            ]
       
        )
   destino_template =  ft.NavigationRailDestination(
            icon=ft.Icons.TASK_ALT,
            selected_icon=ft.Icons.TASK_ALT_OUTLINED,
            label=nome_do_Kanbam
        )
   chaves_telas = list(telas.keys())
   ultimo = int(chaves_telas[-1])+1
   telas[f"{str(ultimo)}"] = template_view
   destinos.append(destino_template)
   page.update()
   page.close(painel_de_criacao)







##############################fim da criação###################################################################

##################################componentes##########################


criar_botao = ft.ElevatedButton(
                    "criar",
                    style = ft.ButtonStyle(bgcolor = ft.Colors.BLACK38),
                    on_click=criar_kanban,disabled=True,tooltip="Só é possivel criar 8 kanbans \n o numero de colunas deve ser igual a quantidade de cores escolhida"
                )

slider = ft.Slider(
                              
                    min=2,
                    max=4,
                    divisions=2,
                    inactive_color=ft.Colors.GREY_900,
                    active_color=ft.Colors.WHITE,
                    overlay_color=ft.Colors.BLACK,
                    label="{value}",on_change=desabilita_botão_criar
                )
green = ft.Checkbox(
    label="",
    on_change=desabilita_botão_criar,
    fill_color=ft.Colors.GREEN,
    shape=ft.CircleBorder(),value=False,
)

red = ft.Checkbox(
    label="",
    on_change=desabilita_botão_criar,
    fill_color=ft.Colors.RED,
    shape=ft.CircleBorder(),value=False
)

yellow = ft.Checkbox(
    label="",
    on_change=desabilita_botão_criar,
    fill_color=ft.Colors.YELLOW,
    shape=ft.CircleBorder(),value=False
)

orange = ft.Checkbox(
    label="",
   on_change=desabilita_botão_criar,
    fill_color=ft.Colors.ORANGE,
    shape=ft.CircleBorder(),value=False
)

blue = ft.Checkbox(
    label="",
    fill_color=ft.Colors.BLUE,
    shape=ft.CircleBorder(),value=False,on_change=desabilita_botão_criar
)
nome_kamb =ft.TextField(
      
        label='nome do KANBAN',
        label_style = ft.TextStyle(font_family="Kanit"),
        icon='TASK_ALT'
    )


##############################fim dos componentes############################################


##########################listas##############################################################################

                                    




kanbans = [
    # função da lista de kanbans vai aqui
ft.Container(
        width=220,
        height=150,
        bgcolor=ft.Colors.PURPLE,
        padding = 20,
        border=ft.border.all(2, ft.Colors.DEEP_PURPLE_500),
        border_radius=10,
        content=ft.Column(
            [
                ft.TextField(
                    "Kanban Template",
                    bgcolor=ft.Colors.DEEP_PURPLE_500,
                    read_only = True,
                    label = "Nome do Kanban",
                    icon=ft.Icons.TASK_ALT,
                    label_style = ft.TextStyle(
                        color = ft.Colors.WHITE,
                        size = 15,
                        italic=True
                    ),
                    text_style = ft.TextStyle(
                        color=ft.Colors.WHITE,
                        size=12,
                    )
                ), # TextField
                # funcao go linkada ao index do view
                ft.TextButton(
                    "GO",
                    icon=ft.Icons.MOVING,
                    style = ft.ButtonStyle(
                        bgcolor = ft.Colors.DEEP_PURPLE_500
                    ),
                    on_click=lambda e: page.go('2')
                )
            ]
        ) # Column
    )
      # Container
                                                        ]
destinos = [
        ft.NavigationRailDestination(
            icon=ft.Icons.LIST,
            selected_icon=ft.Icons.LIST_OUTLINED,
            label="INICIO"
        ),
        ft.NavigationRailDestination(
            icon=ft.Icons.PERSON,
            selected_icon=ft.Icons.PERSON_OUTLINED,
            label="MEMBROS"
        ),
        #TESTE
        ft.NavigationRailDestination(
            icon=ft.Icons.TASK_ALT,
            selected_icon=ft.Icons.TASK_ALT_OUTLINED,
            label="KANBAN TEMPLATE"
        ),
    ]
membros = [
                                            ft.Container(
                                                width=250,
                                                height=250,
                                                bgcolor=ft.Colors.PURPLE,
                                                padding = 20,
                                                border=ft.border.all(2, ft.Colors.DEEP_PURPLE_500),
                                                border_radius=10,
                                                content=ft.Column(
                                                    [
                                                        ft.TextField(
                                                            "Pedro",
                                                            bgcolor=ft.Colors.DEEP_PURPLE_500,
                                                            read_only = True,
                                                            label = "Menbro",
                                                            icon=ft.Icons.PERSON_2,
                                                            label_style = ft.TextStyle(
                                                                color = ft.Colors.WHITE,
                                                                size = 15,
                                                                italic=True
                                                            ),
                                                            text_style = ft.TextStyle(
                                                                color=ft.Colors.WHITE,
                                                                size=12,
                                                            )
                                                        ), # TextField
                                                        ft.TextField(
                                                            "deve o agiota",
                                                            label = "Atividades",
                                                            label_style = ft.TextStyle(
                                                                color = ft.Colors.WHITE,
                                                                size = 15,
                                                                italic=True
                                                            ),
                                                            multiline = True,
                                                            icon=ft.Icons.LIST_ALT_ROUNDED,
                                                            bgcolor = ft.Colors.DEEP_PURPLE_500
                                                        ) # TextField
                                                    ]
                                                ) # Column
                                            ) # Container
                                        ]


###########################################################fim das listas###################################


def init(p):
    global page, telas
#funão de adicionar views linkada ao navigation rail
    page = p
    telas = {
        '0': tela_cadastro.view(),
        '1': tela_tabela.view(),
        '2': ft.View(
            "tela2",
            controls =[
                ft.AppBar(
                    leading=ft.Icon(ft.Icons.TASK_ALT),
                    leading_width=100,
                    actions=[
                        #botão salvar, adicionar função
                        ft.IconButton(
                            ft.Icons.SAVE,
                            icon_color=ft.Colors.WHITE,
                            icon_size=30,on_click=lambda e: print("teste gay")
                        ),
                        #botão apagar adicionar função
                        ft.IconButton(
                            icon=ft.Icons.DELETE_FOREVER_ROUNDED,
                            icon_color=ft.Colors.WHITE,
                            icon_size=30,)
                    ],
                    title=ft.Text(
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
                                            [ft.Colors.BLACK, ft.Colors.PURPLE]
                                        )
                                    ),
                                ),
                            ),
                        ],
                    ),
                    center_title=False,
                    toolbar_height=55,
                    bgcolor=ft.Colors.PURPLE_300,
                ),
                ft.Row(
                    [
                        rail,
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
                                        ft.Text("TESTE"),
                                        ft.Column(
                                            [
                                                ft.Row(
                                                #função de listas vai aqui
                                                    [
                                                        # main container
                                                        ft.Container(
                                                            width=250,
                                                            margin=60,
                                                            height=250,
                                                            border=ft.border.all(2, ft.Colors.PURPLE),
                                                            border_radius = 10,
                                                            padding = 10,
                                                            bgcolor=ft.Colors.ORANGE_400,
                                                            content=ft.DragTarget(
                                                                on_accept=drag_accept,
                                                                content=ft.Draggable(
                                                                    ft.Column(
                                                                        controls = [
                                                                            ft.TextField(
                                                                                "",
                                                                                bgcolor = ft.Colors.WHITE,
                                                                                label = "[Atividadde]:",
                                                                                label_style = ft.TextStyle(
                                                                                    color = ft.Colors.BLACK,
                                                                                    size = 15,
                                                                                    italic = True
                                                                                ),
                                                                                text_style = ft.TextStyle(
                                                                                    color = ft.Colors.BLACK,
                                                                                    size = 12,
                                                                                )
                                                                            ),
                                                                            ft.TextField(
                                                                                "",
                                                                                bgcolor = ft.Colors.WHITE,
                                                                                label = "[Responsavel]:",
                                                                                icon = ft.Icon(
                                                                                    name = ft.Icons.ARROW_CIRCLE_RIGHT,
                                                                                    color = ft.Colors.WHITE,
                                                                                    size = 30,
                                                                                    tooltip = "mover"
                                                                                ),
                                                                                label_style = ft.TextStyle(
                                                                                    color = ft.Colors.BLACK,
                                                                                    size = 12,
                                                                                    italic=True
                                                                                ),
                                                                                text_style = ft.TextStyle(
                                                                                    color = ft.Colors.BLACK,
                                                                                    size=12
                                                                                    )
                                                                            ),
                                                                            ft.TextField(
                                                                                "",
                                                                                label = "[Descrição]:",
                                                                                label_style = ft.TextStyle(
                                                                                    color = ft.Colors.BLACK,
                                                                                    size = 15,
                                                                                    italic=True
                                                                                ),
                                                                                multiline = True,
                                                                                bgcolor = ft.Colors.WHITE,
                                                                                text_style = ft.TextStyle(
                                                                                    color=ft.Colors.BLACK,
                                                                                    size=12
                                                                                )
                                                                            )
                                                                        ]
                                                                    )
                                                                ),
                                                            )
                                                        ),
                                                        # main container
                                                        ft.Container(
                                                            width=250,
                                                            margin=60,
                                                            height=250,
                                                            border=ft.border.all(2, ft.Colors.PURPLE),
                                                            border_radius=10,
                                                            padding=10,
                                                            bgcolor=ft.Colors.ORANGE_400,
                                                            content=ft.DragTarget(
                                                                on_accept=drag_accept,
                                                                content=ft.Draggable(
                                                                    ft.Column(
                                                                        controls = [
                                                                            ft.TextField(
                                                                                "",
                                                                                bgcolor=ft.Colors.WHITE,
                                                                                label = "[Atividadde]:",
                                                                                label_style = ft.TextStyle(
                                                                                    color=ft.Colors.BLACK,
                                                                                    size=15, italic=True
                                                                                ),
                                                                                text_style=ft.TextStyle(
                                                                                    color=ft.Colors.BLACK,
                                                                                    size=12,
                                                                                )
                                                                            ),
                                                                            ft.TextField(
                                                                                "",
                                                                                bgcolor=ft.Colors.WHITE,
                                                                                label="[Responsavel]:",
                                                                                icon= ft.Icon(
                                                                                    name=ft.Icons.ARROW_CIRCLE_RIGHT,
                                                                                    color=ft.Colors.WHITE,
                                                                                    size=30,
                                                                                    tooltip="mover"
                                                                                ),
                                                                                label_style=ft.TextStyle(
                                                                                    color=ft.Colors.BLACK,
                                                                                    size=12,
                                                                                    italic=True
                                                                                ),
                                                                                text_style=ft.TextStyle(
                                                                                    color=ft.Colors.BLACK,
                                                                                    size=12,
                                                                                    )
                                                                            ),
                                                                            ft.TextField(
                                                                                "",
                                                                                label="[Descrição]:",
                                                                                label_style=ft.TextStyle(
                                                                                    color=ft.Colors.BLACK,
                                                                                    size=15,
                                                                                    italic=True
                                                                                ),
                                                                                multiline=True,
                                                                                bgcolor=ft.Colors.WHITE,
                                                                                text_style=ft.TextStyle(
                                                                                    color=ft.Colors.BLACK,
                                                                                    size=12
                                                                                )
                                                                            )
                                                                        ]
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                        ft.FloatingActionButton(
                                                            icon=ft.Icons.ADD,
                                                            tooltip="adicionar cartão na linha",
                                                            on_click=lambda e: page.open(painel_de_criacao2),
                                                            bgcolor=ft.Colors.PURPLE
                                                        )
                                                    ]
                                                ),
                                                ft.FloatingActionButton(
                                                    icon=ft.Icons.ADD,
                                                    tooltip="adicionar cartão na coluna",
                                                    on_click=lambda e: page.open(painel_de_criacao2),
                                                    bgcolor=ft.Colors.PURPLE
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            expand=True
                        ),
                    ],
                    expand=True,
                ) # Row
            ]
       
        )
    }


def controle_de_rota(route_event):
    global tela_atual
    page.views.clear()
    tela_atual = route_event.route

    page.views.append(telas[route_event.route])
    page.update()


def drag_accept(e):
    # get draggable (source) control by its ID
    src = page.get_control(e.src_id)
    print(src.content.controls)
    valor_inicial = e.control.content.content.controls
    e.control.content.content.controls = src.content.controls
    src.content.controls = valor_inicial
    page.update()


##################################### navegação######################################################################
rail = ft.NavigationRail(
    selected_index=None,
    label_type=ft.NavigationRailLabelType.ALL,
    bgcolor=ft.Colors.PURPLE_500,
    min_width=100,
    min_extended_width=400,
    leading=ft.FloatingActionButton(
        icon=ft.Icons.ADD_TASK,
        text="Add",
        on_click = lambda e: page.open(painel_de_criacao)
    ),
    group_alignment=-0.9,
    on_change= lambda e:  page.go(str(e.control.selected_index)),
    # função de destinos
    destinations= destinos
)


def handle_close(e):
    page.close(painel_de_criacao)
    page.add(
        ft.Text(
            f"Modal dialog closed with action: {e.control.text}"
        )
    )


def handle_close2(e):
    page.close(painel_de_criacao2)
    page.add(
        ft.Text(
            f"Modal dialog closed with action: {e.control.text}"
        )
    )
###########################variaveis para o painel##################################################


########################################################################################################

###############################################paine de criação##########################################

painel_de_criacao = ft.AlertDialog(
    modal=True,
    bgcolor = ft.Colors.PURPLE,
    title=ft.Text("BUFAS EXE"),
    #color=ft.Colors.PURPLE
    #content=ft.Text("rato arabe passate a bufa, aceitas ?"),
    content=nome_kamb,
    actions=[
        ft.Row(
            [
         green,
        red,
        yellow,
        orange,
        blue
            ]
        ), # Row
        ft.Row(
            [
                ft.Text("Selecione o numero de colunas:"),
                slider
            ]
        ), # Row
        ft.Row(
            [
            # programar a função criar
               criar_botao,
                ft.ElevatedButton(
                    "cancelar",
                    style = ft.ButtonStyle(bgcolor = ft.Colors.BLACK38),
                    on_click=handle_close
                ),
            ]
        ), # Row
    ],
    #style = ft.ButtonStyle(bgcolor = ft.Colors.PURPLE)
    actions_alignment=ft.MainAxisAlignment.END,
    on_dismiss=lambda e: print("a"),
)


painel_de_criacao2 = ft.AlertDialog(
    modal=True,
    bgcolor = ft.Colors.PURPLE,
    title=ft.Text("BUFAS EXE"),
    # color=ft.Colors.PURPLE
    content=ft.Text("escolha a cor do cartão"),
    actions=[
        ft.Row(
            [
              """  ft.Checkbox(label="",ref=componentes['GREEN'], on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.GREEN,shape= ft.CircleBorder()),
                ft.Checkbox(label="",ref=componentes['RED'], on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.RED,shape= ft.CircleBorder()),
                ft.Checkbox(label="",ref=componentes['WHITE'], on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.WHITE,shape= ft.CircleBorder()),
                ft.Checkbox(label="",ref=componentes['BLACK'], on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.BLACK,shape= ft.CircleBorder()),
                ft.Checkbox(label="",ref=componentes['YELLOW'], on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.YELLOW,shape= ft.CircleBorder()),
                ft.Checkbox(label="",ref=componentes['ORANGE'], on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.ORANGE,shape= ft.CircleBorder()),
                ft.Checkbox(label="",  ref=componentes['BLUE'],on_change=lambda e: print("VOU DEIXAR O OCO"),fill_color=ft.Colors.BLUE,shape= ft.CircleBorder())"""
            ]
        ), # Row
        ft.Row(
            [
                #programar a função criar
                ft.TextButton("criar",style = ft.ButtonStyle(bgcolor = ft.Colors.BLACK38),  on_click=criar_kanban),
                ft.TextButton("cancelar", style = ft.ButtonStyle(bgcolor = ft.Colors.BLACK38),on_click=handle_close2),
            ]
        ) # Row
    ],
    # style = ft.ButtonStyle(bgcolor = ft.Colors.PURPLE)
    actions_alignment=ft.MainAxisAlignment.END,
    on_dismiss=lambda e: page.add(
            ft.Text("reali é gay"),
    ),
)
#########################################utilidades#########################################################

def deletar_kanbam(e):
    tela_deletada = tela_atual
    del telas[tela_deletada]
    destinos.pop(int(tela_deletada))
    for i in list(telas.keys()):
        if int(i)>int(tela_deletada):
            telas[str(int(i)-1)] = telas.pop(str(i))
    rail.selected_index = '0'
    page.go('0')
    page.views.clear()
    page.update()
   

def recuperar_kanbam():
    
    return kanbans

def recuperar_membros():
    
    return membros


#########################################################fim de utilidades#####################################






