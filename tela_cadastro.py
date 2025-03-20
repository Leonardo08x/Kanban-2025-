import flet as ft
import controle as con

#########################################controle de checkbox
def desativar_responsavel(e):
  if check_atividade.value == True:
    check_responsavel.disabled = True
  else:
    check_responsavel.disabled = False
  con.page.update()
def desativar_atividade(e):
  if check_responsavel.value == True:
    check_atividade.disabled = True
  else:
    check_atividade.disabled = False
  con.page.update()
check_responsavel = ft.Checkbox(label="PESQUISAR POR USUARIO", on_change=desativar_atividade,fill_color=ft.Colors.DEEP_PURPLE,shape= ft.CircleBorder(),tooltip="ao selecionar um filtro, o outro ficara desativado, ambos desativados, filtra por nome do kanban")
check_atividade = ft.Checkbox(label="PESQUISAR POR ATIVIDADE", on_change=desativar_responsavel,fill_color=ft.Colors.DEEP_PURPLE,shape= ft.CircleBorder(),tooltip="ao selecionar um filtro, o outro ficara desativado, ambos desativados, filtra por nome do kanban")
###################################################################################################
def view():
    return ft.View(
        "tela0",
        controls =[
            #appbar titulo
            ft.AppBar(
                leading=ft.Icon(ft.Icons.TASK_ALT),
                leading_width=100,
                center_title=False,
                toolbar_height=55,
                bgcolor=ft.Colors.PURPLE_300,
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
                                        [
                                            ft.Colors.BLACK,
                                            ft.Colors.PURPLE
                                        ]
                                    )
                                ),
                            ),
                        ),
                    ]
                )
            ),
            # primeira linha
            ft.Row(expand=True,
                
               controls= [   

                    con.rail ,
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
                                    ft.Column(
                                        [
                                            # Segunda linha, pesquisa, programar a pesquisa
                                            ft.Column(
                                                [
                                                    ft.Row(
                                                    [
                                                        ft.TextField(
                                                                label='pesquisar',
                                                                label_style =  ft.TextStyle(font_family="Kanit"),
                                                                icon='search',
                                                                on_change=pesquisar_kanban,
                                                                bgcolor= ft.Colors.PURPLE_500
                                                            ),check_atividade
                                                           , check_responsavel
                                                        ]
                                                    ), # Row
                                                   con.linha_com_membros
                                                ]
                                            ),
                                            # botão adicionar, incluir em uma linha
                                            ft.FloatingActionButton(
                                                icon=ft.Icons.ADD,
                                                on_click=lambda e: con.page.open(con.painel_de_criacao),
                                                bgcolor=ft.Colors.PURPLE
                                            ),
                                            #incluir aqui a função dos kanbans
                                        ]
                                    ) # Column
                                ]
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        expand=True
                    ) # Column
             ],
             
            tight=True) # Row
        ]
    )
def pesquisar_kanban(e):
    print(con.telas['0'].controls[1].controls[2].controls[0].controls[1].controls[0].controls[1].controls)
    if e.control.value != "":
        resultados_kanbans = []
        if check_responsavel.value == False and check_atividade.value == False:
         for i in list(con.dicionario_de_cartoes.keys()):
          if e.control.value == i.split(',')[1]:
           print("achei")
        elif check_responsavel.value == True:
           for i in list(con.dicionario_de_cartoes.keys()):
            for j in con.dicionario_de_cartoes[i][1]:
               if e.control.value in j:
                print("achei")
         
