import flet as ft
import controle as con
import banco_de_dados as bd
from lista_de_cores import cores

# variaveis globais
indice = 0
botao_salvar_kanban = None


def visualizar_kanban(index : int) -> list:
    global indice
    indice = index
    return [
        ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(f'Tela visualizar kanban: {con.bd[index].get("nome")}'),
                        botao_editar(),
                        botao_salvar(),
                    ]
                ),
                ft.Row(
                    controls=carregar_cartoes(con.bd[index]),
                    vertical_alignment=ft.CrossAxisAlignment.START
                ),
            ],
            alignment=ft.MainAxisAlignment.START
        )
    ]


############################################## criador de cartao #####################################################
def carregar_cartoes(kanban : dict[str, str | list[dict[str, str | list[tuple[str]]]]]) -> list[ft.Container]:
    colunas = []
    for coluna in kanban.get('colunas'):
        # cartoes comecam com o topo da coluna
        cartoes = [container_topo_coluna(coluna.get('nome'), coluna.get('cor'), coluna.get('ID'))]
        # se houver tarefas, serao adicionadas a lista cartoes
        if coluna.get('tarefas'):
            for responsavel, tarefa in coluna.get('tarefas'):
                cartoes.append(container_tarefas(responsavel, tarefa, coluna.get('cor'), coluna.get('ID')))
        # a cada coluna eh adicionada uma ft.Column a lista colunas que sera retornada ao fim da funcao
        colunas.append(
            ft.Column(
                expand=True,
                alignment=ft.MainAxisAlignment.START,
                controls=cartoes
            )
        )
    return colunas


# container do topo da coluna da tela de visualizar kanban
def container_topo_coluna(nome_coluna : str, cor : str, id : str) -> ft.Container:
    return ft.Container(
            width=250,
            height=150,
            bgcolor=cores.get(cor),
            padding = 20,
            border=ft.border.all(2, ft.Colors.DEEP_PURPLE_500),
            border_radius=10,
            expand=True,
            content=ft.Column(
                controls=[
                    # texto com o nome da coluna
                    ft.TextField(
                        label="Coluna",
                        value=nome_coluna,
                        text_style=ft.TextStyle(
                            color=ft.Colors.WHITE,
                            size=15,
                        ),
                        on_change=autorizar_editar_kanban,
                        disabled=True,
                        border="none",
                    ),
                    # botão criar tarefa, em caso de alteracao verificar setor acoes de botoes
                    ft.ElevatedButton(
                        text="Criar tarefa",
                        on_click=abrir_criador_de_tarefas
                    ),
                # adiciona o botão criar apenas na primeira coluna
                ] if id == '0' else [
                    # texto com o nome da coluna
                    ft.TextField(
                        label="Coluna",
                        value=nome_coluna,
                        text_style=ft.TextStyle(
                            color=ft.Colors.WHITE,
                            size=15,
                        ),
                        on_change=autorizar_editar_kanban,
                        disabled=True,
                        border="none",
                    ),
                ],

            ),
        )


# container das tarefas da tela de visualizar kanban
def container_tarefas(responavel : str, tarefa : str, cor : str, id : str) -> ft.Container:
    return ft.Container(
        width=250,
        height=200,
        bgcolor=cores.get(cor),
        padding=10,
        border=ft.border.all(2, ft.Colors.DEEP_PURPLE_500),
        border_radius=10,
        expand=True,
        content=ft.Column(
            controls=[
                # texto com o responsável
                ft.TextField(
                    value=responavel,
                    label="Responsavel",
                    text_style=ft.TextStyle(
                        color=ft.Colors.WHITE,
                        size=15,
                    ),
                    on_change=autorizar_editar_kanban,
                    disabled=True,
                    border="none",
                ),
                # texto com a tarefa
                ft.TextField(
                    value=tarefa,
                    label="Tarefa",
                    text_style=ft.TextStyle(
                        color=ft.Colors.WHITE,
                        size=15,
                    ),
                    on_change=autorizar_editar_kanban,
                    disabled=True,
                    border="none",
                ),
                # botões, em caso de alteracao na estrutura verificar setor acoes de botoes
                ft.Row(
                    controls=botoes_tarefas(id),
                )
            ],
        ),
    )


# container do criador de tarefas
def container_criador_de_tarefas() -> ft.Container:
    return ft.Container(
        width=250,
        height=150,
        bgcolor=ft.Colors.WHITE,
        padding=10,
        border=ft.border.all(2, ft.Colors.DEEP_PURPLE_500),
        border_radius=10,
        expand=True,
        content=ft.Column(
            controls=[
                ft.TextField(
                    label="Responsavel",
                    text_style=ft.TextStyle(
                        color=ft.Colors.DEEP_PURPLE_500,
                        size=15,
                    ),
                    on_change=autorizar_editar_kanban
                ),
                ft.TextField(
                    label="Tarefa",
                    text_style=ft.TextStyle(
                        color=ft.Colors.DEEP_PURPLE_500,
                        size=15,
                    ),
                    on_change=autorizar_editar_kanban
                ),
                # em caso de alteracao na estrutura verificar setor criar e fechar criador de tarefas
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="Criar tarefa",
                            on_click=criar_tarefa
                        ),
                        ft.ElevatedButton(
                            text="Cancelar",
                            on_click=fechar_criador_de_tarefas
                        ),
                    ]
                )
            ],
        ),
    )


########################################## botoes #################################################
def botoes_tarefas(id : str) -> list[ft.ElevatedButton]:
    global indice
    ids = [coluna.get('ID') for coluna in con.bd[indice].get('colunas')]
    
    # em caso de alteracao na estrutura verificar setor acoes dos botoes
    if id == '0':
        return [
            ft.ElevatedButton(
                text="Excluir",
                on_click=excluir_tarefa
            ),
            ft.ElevatedButton(
                text="Avançar",
                on_click=avancar_tarefa
            ),
        ]
    elif id == str(max(ids)):
        return [
            ft.ElevatedButton(
                text="Voltar",
                on_click=voltar_tarefa,
            ),
            ft.ElevatedButton(
                text="Excluir",
                on_click=excluir_tarefa
            ),
        ]
    else:
        return [
            ft.ElevatedButton(
                text="Voltar",
                on_click=voltar_tarefa,
            ),
            ft.ElevatedButton(
                text="Excluir",
                on_click=excluir_tarefa
            ),
            ft.ElevatedButton(
                text="Avançar",
                on_click=avancar_tarefa
            )
        ]


def botao_editar():
    return ft.ElevatedButton(
        text="Editar Kankan",
        on_click=editar_kanban,
    )


def botao_salvar():
    global botao_salvar_kanban
    # botao salvar como global para ser alterado na funcao autorizar_editar_kanban
    botao_salvar_kanban = ft.ElevatedButton(
        text="Salvar",
        on_click=salvar_kanban,
        visible=False
    )
    return botao_salvar_kanban


######################################################### acoes dos botoes ###############################################################
def abrir_criador_de_tarefas(e):
    # elevated_button = e.control -> acessa o elevated_button
    # column_interna = e.control.parent -> acessa a ft.Column que contem o elevated_button
    # container = e.control.parent.parent -> acessa a ft.Container que contem a ft.Column
    # column_externa = e.control.parent.parent.parent -> acessa a ft.Column que contem os ft.Container
    # column_externa_valores = e.control.parent.parent.parent.controls -> acessa o conteudo da ft.Column dos cartoes/ft.Container
    coluna_cartoes = e.control.parent.parent.parent.controls

    # adicionando o container criador de tarefas no primeiro elemento da column
    coluna_cartoes.insert(1, container_criador_de_tarefas())
    
    con.page.update()
    


def voltar_tarefa(e):
    # botao = e.control -> acessa o botao
    # linha = e.control.parent -> acessa a ft.Row que contem o botao
    # coluna = e.control.parent.parent -> acessa a ft.Column que contem a ft.Row
    # conteudo_coluna = e.control.parent.parent.controls -> acessa o conteudo da ft.Column
    conteudo_coluna = e.control.parent.parent.controls

    responsavel = conteudo_coluna[0].value
    tarefa = conteudo_coluna[1].value

    tupla_tarefa = (responsavel, tarefa)

    # acessando o banco de dados
    kanban = con.bd[int(con.page.route) - 2]

    # removendo a tarefa da coluna
    for coluna in kanban.get('colunas')[::-1]:
        tarefas = coluna.get('tarefas')
        if tarefas and tupla_tarefa in tarefas:
            id = coluna.get('ID')
            tarefas.remove(tupla_tarefa)
            break

    # adicionando a tarefa na coluna seguinte
    for coluna in kanban.get('colunas')[::-1]:
        if coluna.get('ID') == str(int(id) - 1):
            coluna.get('tarefas').append(tupla_tarefa)
            break

    # atualizando o banco de dados
    con.carregar_rotas()    


def avancar_tarefa(e):
    # botao = e.control -> acessa o botao
    # linha = e.control.parent -> acessa a ft.Row que contem o botao
    # coluna = e.control.parent.parent -> acessa a ft.Column que contem a ft.Row
    # conteudo_coluna = e.control.parent.parent.controls -> acessa o conteudo da ft.Column
    conteudo_coluna = e.control.parent.parent.controls

    responsavel = conteudo_coluna[0].value
    tarefa = conteudo_coluna[1].value

    tupla_tarefa = (responsavel, tarefa)

    # acessando o banco de dados
    kanban = con.bd[int(con.page.route) - 2]

    # removendo a tarefa da coluna
    for coluna in kanban.get('colunas'):
        tarefas = coluna.get('tarefas')
        if tarefas and tupla_tarefa in tarefas:
            id = coluna.get('ID')
            tarefas.remove(tupla_tarefa)
            break

    # adicionando a tarefa na coluna seguinte
    for coluna in kanban.get('colunas'):
        if coluna.get('ID') == str(int(id) + 1):
            coluna.get('tarefas').append(tupla_tarefa)
            break

    # atualizando o banco de dados
    con.carregar_rotas()    


def excluir_tarefa(e):
    # botao = e.control -> acessa o botao
    # linha = e.control.parent -> acessa a ft.Row que contem o botao
    # coluna = e.control.parent.parent -> acessa a ft.Column que contem a ft.Row
    # conteudo_coluna = e.control.parent.parent.controls -> acessa o conteudo da ft.Column
    conteudo_coluna = e.control.parent.parent.controls

    responsavel = conteudo_coluna[0].value
    tarefa = conteudo_coluna[1].value

    tupla_tarefa = (responsavel, tarefa)

    # acessando o banco de dados
    kanban = con.bd[int(con.page.route) - 2]

    # removendo a tarefa da coluna
    for coluna in kanban.get('colunas'):
        tarefas = coluna.get('tarefas')
        if tarefas and tupla_tarefa in tarefas:
            tarefas.remove(tupla_tarefa)
            break

    # atualizando o banco de dados
    con.carregar_rotas()


def editar_kanban(e):
    # botao = e.control
    # linha_principal_1 = e.control.parent
    linha_principal_1 = e.control.parent
    # coluna_principal = e.control.parent.parent
    # conteudo_coluna_principal = e.control.parent.parent.controls
    # linha_principal_2 = e.control.parent.parent.controls[1]
    # colunas_de_catoes = e.control.parent.parent.controls[1].controls
    colunas_de_catoes = e.control.parent.parent.controls[1].controls

    for coluna in colunas_de_catoes:
        for cartao in coluna.controls:
            coluna_cartao = cartao.content
            for elemento in coluna_cartao.controls:
                if elemento.__class__.__name__ == 'TextField':
                    elemento.disabled = False
                elif elemento.__class__.__name__ == 'ElevatedButton':
                    elemento.disabled = True
                elif elemento.__class__.__name__ == 'Row':
                    for botao in elemento.controls:
                        elemento.disabled = True

    # deixando o botao editar invisivel
    linha_principal_1.controls[1].visible = False
    # deixando o botao salvar visivel
    linha_principal_1.controls[2].visible = True

    con.page.update()


def salvar_kanban(e):
    # botao = e.control
    # linha_principal_1 = e.control.parent
    linha_principal_1 = e.control.parent
    # coluna_principal = e.control.parent.parent
    # conteudo_coluna_principal = e.control.parent.parent.controls
    # linha_principal_2 = e.control.parent.parent.controls[1]
    # colunas_de_catoes = e.control.parent.parent.controls[1].controls
    colunas_de_catoes = e.control.parent.parent.controls[1].controls

    # verificando kanban atual
    kanban = con.bd[int(con.page.route) - 2]


    for i, coluna in enumerate(colunas_de_catoes):
        # pegando o nome da coluna dentro do textfield
        nome_coluna = coluna.controls[0].content.controls[0].value

        # atualizando o nome da coluna no bd
        kanban['colunas'][i]['nome'] = nome_coluna

        # pegando as tarefas da coluna
        tarefas = []
        # eliminando o topo da coluna
        for cartao in coluna.controls[1:]:
            if isinstance(cartao.content.controls[0], ft.TextField)\
            and isinstance(cartao.content.controls[1], ft.TextField):
                novo_responsavel = cartao.content.controls[0].value
                nova_tarefa = cartao.content.controls[1].value
                tarefas.append((novo_responsavel, nova_tarefa))

        # atualizando as tarefas da coluna no bd
        kanban['colunas'][i]['tarefas'] = tarefas
        
        # desabilitando a edicao das tarefas
        for cartao in coluna.controls:
            coluna_cartao = cartao.content
            for elemento in coluna_cartao.controls:
                if isinstance(elemento, ft.TextField):
                    elemento.disabled = True
                elif isinstance(elemento, ft.ElevatedButton):
                    elemento.disabled = False
                elif isinstance(elemento, ft.Row):
                    for botao in elemento.controls:
                        elemento.disabled = False
    

    # deixando o botao editar visivel
    linha_principal_1.controls[1].visible = True
    # deixando o botao salvar invisivel
    linha_principal_1.controls[2].visible = False

    con.carregar_rotas()


############################################# criar e fechar criador de tarefas ############################################################
def fechar_criador_de_tarefas(e):
    # elevated_button = e.control -> acessa o elevated_button
    # row_botoes = e.control.parent -> acessa a ft.Row que contem o elevated_button
    # column = e.control.parent.parent -> acessa a ft.Column que contem os botoes e os textfields de criacao
    # container = e.control.parent.parent.parent -> acessa o ft.Container de criacao
    # column_tarefas_0 = e.control.parent.parent.parent.parent -> acessa a primeira ft.Column que contem as tarefas
    column_tarefas_0 = e.control.parent.parent.parent.parent
    
    # apagando o container criador de tarefas que aparece na 2 posicao/indice 1
    column_tarefas_0.controls.pop(1)

    con.page.update()


def criar_tarefa(e):
    # elevated_button = e.control -> acessa o elevated_button
    # row_interna = e.control.parent -> acessa a ft.Row interna que contem o elevated_button
    # column_interna = e.control.parent.parent -> acessa a ft.Column que contem a ft.Row interna
    # valores_column1 = e.control.parent.parent.controls -> acessa o conteudo da ft.Column que contem o elevated_button e os textfields
    valores_column1 = e.control.parent.parent.controls

    # pegando os dados do alertdialog
    responsavel = valores_column1[0].value
    tarefa = valores_column1[1].value

    # pegando o indice do kanban atraves da rota
    indice = int(con.page.route) - 2
    # pegando o kanban
    kanban = con.bd[indice]
    # criando a tarefa no kanban
    kanban.get('colunas')[0].get('tarefas').append((responsavel, tarefa))

    # atualizando o banco de dados
    bd.editar(indice, con.bd, kanban)

    # atualizando as rotas e os kanbans
    con.carregar_rotas()


################################################## verificacao de campos ############################################################
def autorizar_editar_kanban(e):
    global botao_salvar_kanban
    textfield = e.control

    if textfield.value == '':
        botao_salvar_kanban.disabled = True
    else:
        botao_salvar_kanban.disabled = False

    con.page.update()