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
    # gridview1 = alerta_dialog.content.controls[2] -> recebe o gridview da coluna
    gridview_valores = alerta_dialog.content.controls[2].controls
    # diferenca da quantidade de colunas com o slider
    colunas_extras = int(slider_colunas.value) - len(gridview_valores)//2
    # se mudar para mais colunas, adiciona o textfield e as cores
    if colunas_extras > 0:
        gridview_valores.extend(
            [
                ft.TextField(
                    label=f'Coluna {len(gridview_valores)//2 + 1}',
                    on_change=autorizar_criar_kanban
                ),
                # checkbox para escolher as cores
                ft.GridView(
                    runs_count=4,
                    controls=cores_checkbox(),
                ),
            ]
        )
    # se mudar para menos colunas, remove o textfield e as cores
    else:
        gridview_valores.pop() # remove as cores
        gridview_valores.pop() # remove o textfield

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
    # gridview1 = alerta_dialog.content.controls[2] -> recebe o gridview da coluna
    textfields = alerta_dialog.content.controls[2].controls[::2]
    # gridview2 = gridview1.controls[1::2] -> recebe uma lista dos gridview das cores
    gridview2 = alerta_dialog.content.controls[2].controls[1::2]

    # lista com as cores escolhidas
    cores_valores = [
        checkbox.value
        for checkboxes in gridview2
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
    gridview1_valores = alerta_dialog.content.controls[2].controls # recebe a lista de valores do gridview1 da coluna

    # fechar caixas de dialogo
    alerta_dialog.open = False
    
    # limpa a caixa de texto do nome do kanban
    column.controls[0].value = ''

    # limpa as caixas de texto dos nomes das colunas
    for textfield in gridview1_valores[::2]:
        textfield.value = ''

    # desmarca o slider
    slider_colunas.value = 2
    
    # desmarca as cores
    for gridview2 in gridview1_valores[1::2]:
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
        for nome_coluna in gridview1_valores[::2]
    ]
    
    # pega as cores
    cores_selecionadas = [
        checkbox.data
        for gridview2 in gridview1_valores[1::2]
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
    title=ft.Text('Criar um novo kanban'),
    content=ft.Column(
        controls=[
            ft.TextField(
                label='Nome do kanban',
                autofocus=True,
                on_change=autorizar_criar_kanban
            ),
            ft.Divider(),
            ft.GridView(
                runs_count=2,
                controls=[
                    ft.TextField(
                        label='Coluna 1',
                        on_change=autorizar_criar_kanban,
                    ),
                    ft.GridView(
                        runs_count=4,
                        controls=cores_checkbox()
                    ),
                    ft.TextField(
                        label='Coluna 2',
                        on_change=autorizar_criar_kanban,
                    ),
                    ft.GridView(
                        runs_count=4,
                        controls=cores_checkbox()
                    ),
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

