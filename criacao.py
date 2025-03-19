import flet as ft
import controle as con
from lista_de_cores import cores
from bd import bd



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
            'Cancelar',
            on_click=fechar_alerta_dialog
        )
    ]


def autorizar_criar_kanban(e=None):
    global alerta_dialog, slider_colunas, cores_checkbox, botao_criar
    # verifica se o nome do kanban foi preenchido e se o slider e as cores tem quantidades iguais
    if alerta_dialog.content.value and slider_colunas.value == sum(cor.value for cor in cores_checkbox):
        botao_criar.disabled = False
    else:
        botao_criar.disabled = True
    
    # atualiza a pagina para atualizar o botao
    con.page.update()


def fechar_alerta_dialog(e):
    global alerta_dialog, cores_checkbox, botao_criar
    # fechar caixa de dialogo
    alerta_dialog.open = False
    
    # limpa o caixa de texto
    alerta_dialog.content.value = ''
    
    # desmarca as cores
    for cor in cores_checkbox:
        cor.value = False

    # desativa o botao de criar
    botao_criar.disabled = True
        
    # atualiza a pagina
    con.page.update()


def criar_kanban(e):
    global alerta_dialog, slider_colunas, cores_checkbox
    # pega o nome do kanban
    nome = alerta_dialog.content.value

    # pega o numero de colunas
    num_colunas = slider_colunas.value

    # pega as cores
    cores_selecionadas = [
        cor.data
        for cor in cores_checkbox
        if cor.value
    ]

    # adiciona o kanban ao banco de dados
    bd.append(
        {
            'nome': nome,
            'colunas': [
                {
                    'nome': f'coluna {coluna+1}',
                    'cor': cores_selecionadas[coluna],
                    'tarefas': []
                }
                for coluna in range(int(num_colunas))
            ]
        }
    )
    
    
    # fechar caixa de dialogo e atualizar a pagina
    fechar_alerta_dialog(e)

    # atualiza as rotas do navigation rail para então carregar o novo kanban
    con.carregar_rotas()
    

# variaveis globais
# cria os Checkbox para escolher as cores a partir do dicionario cores
cores_checkbox = [
    ft.Checkbox(
        fill_color=codigo,
        shape=ft.CircleBorder(),
        value=False,
        data=cor,
        on_change=autorizar_criar_kanban,
    )
    for cor, codigo in cores.items()
]


# caixa de dialogo para criação de kanbans
alerta_dialog = ft.AlertDialog(
    modal=True,
    title=ft.Text('Criar um novo kanban'),
    content=ft.TextField(
        label='Nome do kanban',
        autofocus=True,
        on_change=autorizar_criar_kanban
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
                    on_change=autorizar_criar_kanban
                ),
            ],
            expand=True,
        ),
        # checkbox para escolher as cores
        ft.Row(
            controls=cores_checkbox,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            expand=True,
        ),
        # botoes criar ou cancelar
        ft.Row(
            controls=botoes(),
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            expand=True,
        )
    ],
    actions_alignment=ft.MainAxisAlignment.END,
)


# atualiza o numero de colunas dinamicamente
slider_colunas = alerta_dialog.actions[0].controls[1]