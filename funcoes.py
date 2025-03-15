import controle as con


def deletar_kanbam(e):
    tela_deletada = con.tela_atual
    del con.telas[tela_deletada]
    con.destinos.pop(int(tela_deletada))
    for i in list(con.telas.keys()):
        if int(i) > int(tela_deletada):
            con.telas[str(int(i)-1)] = con.telas.pop(str(i))
    con.page.views.clear()
    con.rail.selected_index = '0'
    con.page.go('0')
    con.page.update()