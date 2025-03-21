import flet as ft
import banco_de_dados as bd


def main(page : ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "teste"
    
    
    def prencher_coluna(e):
        '''
            Essa função atualiza a caixa de seleção coluna em dunção do ID do kanban
        '''
        for kanban in bd.carregar():
            if kanban["ID"] == caixa_selecao_kanban.value:
                #Atualizo a caixa de seleção
                #os itens da lista serão dropdown.Options com os parâmetro key, text
                #O parâmetro text será a opção que o usuário verá e poderá escolher
                #Quando o usuário escolher alguma opção, o argumento passado no parâmetro key
                #Será trasnferido para o ft.Dropdown que o engloba
                nome_coluna = [(coluna["ID"],coluna["nome"]) for coluna in kanban["colunas"]]
                caixa_selecao_coluna.options = [ft.dropdown.Option(key= item[0],text= item[1])
                                                 for item in nome_coluna]
                
                #Ativo a segunda caixa de seleção
                caixa_selecao_coluna.disabled = False
                
                page.update()
                #Como o ID é único, o return serve para parar a iteração
                return None
    
    
    def lista_kanban():
        '''
            Essa função atualiza a caixa de seleção dos kanbans conforme o banco de dados
            mas pode ser alterada para funcionar com outra variável 
        '''
        lista_nomes_ID = [(kanban["ID"], kanban["nome"]) for kanban in bd.carregar()]
        caixa_selecao_kanban.options = [ft.dropdown.Option(item[0], item[1]) 
                                        for item in lista_nomes_ID]
        

    #As caixas de seleção serão dropdowns e suas opções está no parâmetro options
    #Mas esse option, será atualizado em tempo real pelas funções
    caixa_selecao_kanban = ft.Dropdown(label= "Kanbans")
        
    caixa_selecao_coluna = ft.Dropdown(label= "Colunas", disabled= True)
    
    #Utilizei um botão para atualizar a caixa de seleção das colunas, pois quando tentei
    #fazer direto pelo dropdown, estava dando erro, então pela falta de tempo, fiz isso
    pesquisa_coluna = ft.ElevatedButton("search", on_click= prencher_coluna)
    
    #Chamo a função para atualizar a caixa de selecao dos kanbans
    lista_kanban()
    
    #Adiciono os elementos na página
    page.add(
        ft.Row([caixa_selecao_kanban, pesquisa_coluna]),
        ft.Row([caixa_selecao_coluna])
    )
    

ft.app(main)