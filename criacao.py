import flet as ft
import controle as con

def criar_kanban(e):
    cores = []
    nome_do_Kanbam = nome_kamb.value
    limite = int(slider.value)

    if blue.value:
        cores.append(ft.Colors.BLUE)
        blue.value = False

    if green.value:
        cores.append(ft.Colors.GREEN)
        green.value = False

    if red.value:
        cores.append(ft.Colors.RED)
        red.value = False

    if yellow.value:
        cores.append(ft.Colors.YELLOW)
        yellow.value = False

    if orange.value:
        cores.append(ft.Colors.ORANGE)
        orange.value = False

    
    chaves_telas = list(con.telas.keys())
    ultimo = int(chaves_telas[-1])+1
    con.telas[f"{str(ultimo)}"] = con.tela_teste.view(limite, cores, nome_do_Kanbam)
    con.destinos.append(
        ft.NavigationRailDestination(
            icon=ft.Icons.TASK_ALT,
            selected_icon=ft.Icons.TASK_ALT_OUTLINED,
            label=nome_do_Kanbam
        )
    )

    con.page.update()
    con.page.close(painel_de_criacao)
    nome_kamb.value = None
    
    slider.value = 2


def handle_close(e):
    con.page.close(painel_de_criacao)
    con.page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))


def desabilita_botão_criar(e):
    cores = [blue.value, green.value, red.value, yellow.value, orange.value]

    if len(list(con.telas.keys()))<10 and sum(cores) == int(slider.value):
        criar_botao.disabled = False
    else:
        criar_botao.disabled = True

    con.page.update()


green = ft.Checkbox(
    fill_color=ft.Colors.GREEN,
    shape=ft.CircleBorder(),
    value=False,
    on_change=desabilita_botão_criar
)


red = ft.Checkbox(
    fill_color=ft.Colors.RED,
    shape=ft.CircleBorder(),
    value=False,
    on_change=desabilita_botão_criar
)


yellow = ft.Checkbox(
    fill_color=ft.Colors.YELLOW,
    shape=ft.CircleBorder(),
    value=False,
    on_change=desabilita_botão_criar
)

orange = ft.Checkbox(
    fill_color=ft.Colors.ORANGE,
    shape=ft.CircleBorder(),
    value=False,
    on_change=desabilita_botão_criar
)


blue = ft.Checkbox(
    fill_color=ft.Colors.BLUE,
    shape=ft.CircleBorder(),
    value=False,
    on_change=desabilita_botão_criar
)


slider = ft.Slider(
    min=2,
    max=4,
    divisions=2,
    inactive_color=ft.Colors.GREY_900,
    active_color=ft.Colors.WHITE,
    overlay_color=ft.Colors.BLACK,
    label="{value}",
    on_change=desabilita_botão_criar
)


criar_botao = ft.ElevatedButton(
    "criar",
    style = ft.ButtonStyle(bgcolor = ft.Colors.BLACK38),
    on_click=criar_kanban,
    disabled=True,
    tooltip="Só é possivel criar 8 kanbans\no numero de colunas deve ser igual a quantidade de cores escolhida"
)


nome_kamb = ft.TextField(
    label='Nome do KANBAN',
    label_style = ft.TextStyle(font_family="Kanit"),
    icon='TASK_ALT'
)


painel_de_criacao = ft.AlertDialog(
    modal=True,
    bgcolor = ft.Colors.PURPLE,
    title=ft.Text("BUFAS EXE"),
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
                )
            ]
        ) # Row
    ],
    actions_alignment=ft.MainAxisAlignment.END,
    on_dismiss=lambda e: print("kanban criado com sucesso"),
)
