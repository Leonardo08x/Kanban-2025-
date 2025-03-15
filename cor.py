import flet as ft
import controle as con

def desabilita_botão_criar(e):
    cores = []
    nome_do_Kanbam : str = con.nome_kamb.value
    limite = int(slider.value)

    if blue.value:
        cores.append(ft.Colors.BLUE)

    if green.value:
        cores.append(ft.Colors.GREEN )

    if red.value:
        cores.append(ft.Colors.RED)

    if yellow.value:
        cores.append(ft.Colors.YELLOW)

    if orange.value:
        cores.append(ft.Colors.ORANGE)

    if len(list(con.telas.keys()))<10:
        if len(cores) == limite:
            con.criar_botao.disabled = False
        else:
            con.criar_botao.disabled = True
    else:
        con.criar_botao.disabled = True

    con.page.update()


green = ft.Checkbox(
    label="",
    fill_color=ft.Colors.GREEN,
    shape=ft.CircleBorder(),
    value=False,
    on_change=desabilita_botão_criar
)


red = ft.Checkbox(
    label="",
    fill_color=ft.Colors.RED,
    shape=ft.CircleBorder(),
    value=False,
    on_change=desabilita_botão_criar
)


yellow = ft.Checkbox(
    label="",
    fill_color=ft.Colors.YELLOW,
    shape=ft.CircleBorder(),
    value=False,
    on_change=desabilita_botão_criar
)

orange = ft.Checkbox(
    label="",
    fill_color=ft.Colors.ORANGE,
    shape=ft.CircleBorder(),
    value=False,
    on_change=desabilita_botão_criar
)


blue = ft.Checkbox(
    label="",
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

