import flet as ft
import controle as con
from lista_de_cores import cores


############################## componentes ##############################
def botoes():
    global botao_criar
    # botao criar como global para ser alterado na funcao autorizar_criar_kanban
    botao_criar = ft.ElevatedButton(
            text='Criar',
            on_click=criar_kanban,
            disabled=True,
        )
    # cria os botoes de criar e cancelar
    return [
        botao_criar,
        ft.ElevatedButton(
            text='Cancelar',
            on_click=fechar_alerta_dialog
        )
    ]


# cria os Checkbox para escolher as cores a partir do dicionario cores
def cores_checkbox() -> list[ft.Checkbox]:
    return [
        ft.Checkbox(
            fill_color=codigo,
            shape=ft.CircleBorder(),
            value=False,
            data=cor,
            on_change=mudanca_cores,
        )
        for cor, codigo in cores.items()
    ]


#################################### funcoes de alteracao ####################################
def mudanca_slider(e):
    global slider_colunas, alerta_dialog
    # column = alerta_dialog.content -> recebe a coluna do alerta dialogo
    # linha = alerta_dialog.content.controls[2] -> recebe a linha da coluna
    linha_valores = alerta_dialog.content.controls[2].controls
    # diferenca da quantidade de colunas com o slider
    colunas_extras = int(slider_colunas.value) - len(linha_valores)//3
    # se mudar para mais colunas, adiciona o textfield e as cores
    if colunas_extras > 0:
        linha_valores.extend(
            [
                ft.TextField(
                    width=150,
                    label=f'Coluna {len(linha_valores)//3 + 1}',
                    on_change=autorizar_criar_kanban,
                    border_radius=15,
                    border_color=ft.Colors.WHITE70,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.Colors.WHITE70,
                    label_style=ft.TextStyle(
                        color=ft.Colors.WHITE70,
                        decoration=ft.TextDecoration.UNDERLINE,
                        decoration_color=ft.Colors.WHITE70,
                        size=15,
                        italic=True)

                ),
                # checkbox para escolher as cores
                ft.GridView(
                    runs_count=5,
                    width=150,
                    controls=cores_checkbox(),
                ),
                ft.Divider(opacity=0.5),
            ]
        )
    # se mudar para menos colunas, remove o textfield, as cores e o divisor
    else:
        # remove o textfield, as cores e o divisor que estao por ultimo na linha
        del linha_valores[-3:]

    # verifica a validade dos dados para ativar o botao criar
    autorizar_criar_kanban(e)


def mudanca_cores(e):
    global alerta_dialog
    chechbox_selecionada = e.control
    chechboxes = e.control.parent.controls
    # desmarca a cor selecionada anteriormente
    for checkbox in chechboxes:
        if checkbox != chechbox_selecionada:
            checkbox.value = False
    # verifica a validade dos dados para ativar o botao criar
    autorizar_criar_kanban(e)


def autorizar_criar_kanban(e):
    global alerta_dialog, slider_colunas, botao_criar
    # column = alerta_dialog.content -> recebe a coluna do alerta dialogo
    textfield_kanban = alerta_dialog.content.controls[0]
    # linha = alerta_dialog.content.controls[2] -> recebe a linha da coluna
    textfields = alerta_dialog.content.controls[2].controls[::3]
    # gridview = linha.controls[1::3] -> recebe uma lista dos gridview das cores
    gridviews = alerta_dialog.content.controls[2].controls[1::3]

    # lista com as cores escolhidas
    cores_valores = [
        checkbox.value
        for checkboxes in gridviews
        for checkbox in checkboxes.controls
        if checkbox.value
    ]

    # lista com todos os nomes das colunas
    valores_coluna = [
        textfields[i].value
        for i in range(int(slider_colunas.value))
    ]
    
    # verifica se o nome do kanban foi preenchido e se o slider e as cores tem quantidades iguais
    if textfield_kanban.value\
    and len(textfield_kanban.value) <= 10\
    and len(cores_valores) == int(slider_colunas.value)\
    and all(valores_coluna):
        botao_criar.disabled = False
    else:
        botao_criar.disabled = True
    
    # atualiza a pagina para atualizar o botao
    con.page.update()


####################################### funcoes dos botoes do alerta dialogo #######################################
def fechar_alerta_dialog(e):
    global alerta_dialog, slider_colunas, botao_criar
    column = alerta_dialog.content # recebe a coluna do alerta dialogo
    row_valores = alerta_dialog.content.controls[2].controls # recebe a lista de valores da row da coluna

    # fechar caixas de dialogo
    alerta_dialog.open = False
    
    # limpa a caixa de texto do nome do kanban
    column.controls[0].value = ''

    # apaga as caixas de texto extras
    if len(row_valores) > 6:
        del row_valores[6:]
        
    # limpa as caixas de texto dos nomes das colunas
    for textfield in row_valores[::3]:
        textfield.value = ''

    # desmarca o slider
    slider_colunas.value = 2
    
    # desmarca as cores
    for gridview2 in row_valores[1::3]:
        for checkbox in gridview2.controls:
            checkbox.value = False

    # desativa o botao de criar
    botao_criar.disabled = True
        
    # atualiza a pagina
    con.page.update()


def criar_kanban(e):
    global alerta_dialog, slider_colunas
    # cria o ID
    def criar_ID_kanban() -> str:
        if not con.bd:
            # primeiro ID sempre 0
            return '0'
        else:
            ids = [int(kanban.get('ID')) for kanban in con.bd]
            for i in range(max(ids)+1):
                if i not in ids:
                    return str(i)
            else:
                return str(max(ids)+1)
            
    column = alerta_dialog.content # recebe a coluna do alerta dialogo
    gridview1_valores = alerta_dialog.content.controls[2].controls # recebe a lista de valores do gridview da coluna

    # pega o nome do kanban
    nome = column.controls[0].value

    # pega o numero de colunas
    num_colunas = int(slider_colunas.value)

    # pega os nomes das colunas
    nome_colunas = [
        nome_coluna.value
        for nome_coluna in gridview1_valores[::3]
    ]
    
    # pega as cores
    cores_selecionadas = [
        checkbox.data
        for gridview2 in gridview1_valores[1::3]
        for checkbox in gridview2.controls 
        if checkbox.value
    ]
    
    # fechar caixa de dialogo e atualizar a pagina
    fechar_alerta_dialog(e)

    # adiciona o kanban ao banco de dados
    con.bd.append(
        {
            'nome': nome,
            'ID': criar_ID_kanban(),
            'colunas': [
                {
                    'nome': nome_colunas[index],
                    'ID': str(index),
                    'cor': cores_selecionadas[index],
                    'tarefas': []
                }
                for index in range(num_colunas)
            ]
        }
    )

    # atualiza as rotas do navigation rail para então carregar o novo kanban
    con.carregar_rotas()

    # vai para o kanban criado
    con.page.go(str(len(con.bd)+1))

    

################################### alerta dialogo para criação de kanbans ###################################
# caixa de dialogo para criação de kanbans
alerta_dialog = ft.AlertDialog(
    modal=True,
    bgcolor = ft.Colors.INVERSE_PRIMARY,
    title=ft.Text('Criar um novo kanban',text_align=ft.TextAlign.CENTER,),
    content=ft.Column(
        width=350,
        height=500,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.TextField(
                icon=ft.Icons.TASK_ALT,
                label='Nome do kanban',
                text_align=ft.TextAlign.CENTER,
                color=ft.Colors.WHITE70,
                border_color = ft.Colors.WHITE70,
                autofocus=True,
                helper_text ='minimo de 1 caractere maximo de 10 caracteres',
                on_change=autorizar_criar_kanban
            ),
            ft.Divider(),
            ft.Row(
                expand=True,
                wrap=True,
                controls=[
                    ft.TextField(
                        width=150,
                        on_change=autorizar_criar_kanban,
                        label='Coluna 1:',
                        border_radius=15,
                        border_color = ft.Colors.WHITE70,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.WHITE70,
                        label_style = ft.TextStyle(
                            color = ft.Colors.WHITE70,
                            decoration=ft.TextDecoration.UNDERLINE,
                            decoration_color=ft.Colors.WHITE70,
                            size = 15,
                            italic=True
                        )
                    ),
                    ft.GridView(
                        runs_count=5,
                        width=150,
                        controls=cores_checkbox()
                    ),
                    ft.Divider(opacity=0.5),
                    ft.TextField(
                        width=150,
                        label='Coluna 2',
                        on_change=autorizar_criar_kanban,
                        border_radius = 15,
                        text_align=ft.TextAlign.CENTER,
                        border_color = ft.Colors.WHITE70,
                        color=ft.Colors.WHITE70,
                        label_style=ft.TextStyle(
                            color=ft.Colors.WHITE70,
                            decoration=ft.TextDecoration.UNDERLINE,
                            decoration_color=ft.Colors.WHITE70,
                            size=15,
                            italic=True)
                    ),
                    ft.GridView(
                        runs_count=5,
                        width=150,
                        controls=cores_checkbox()
                    ),
                    ft.Divider(opacity=0.5),
                ]
            )
        ],
    ),
    actions=[
        # slider para escolher o numero de colunas
        ft.Column(
            controls=[
                ft.Text("Selecione o numero de colunas:"),
                ft.Slider(
                    min=2,
                    max=5,
                    divisions=3,
                    label='{value}',
                    on_change=mudanca_slider
                ),
                # botoes criar ou cancelar
                ft.Row(
                    controls=botoes(),
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    expand=True,
                )
            ],
        ),
    ],
)


# atualiza o numero de colunas dinamicamente
slider_colunas = alerta_dialog.actions[0].controls[1]

