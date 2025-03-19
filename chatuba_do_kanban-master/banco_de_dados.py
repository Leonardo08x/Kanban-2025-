
import os


#incompleto e falho
dicionario_de_cartoes = {
    "{indice},{nome}" : [ ["{cor}"], ["{atividade}"], ["{responsáveis}"], ["{descrições}"]]
}

#Mais completo
dicionario = {
    "{indice},{nome}" : {
        "{coln},{coluna}" : [["{cor}"], ["{atividades}"], ["{responsáveis}"], ["{descrições}"]]
    }
}

'''
    /Kanbans -> pasta de todos os kanbans
        /{indice},{nome} -> pasta do kanban {nome}
            /{coln},{coluna}.txt -> arquivo de texto referente a coluna {coluna}
                {nome da cor}
                {atividade 1};{atividade 2};{atividade 3};...
                {responsavel 1};{reponsavel 2};-;{responsavel 3};...
                {descrição 1};{descrição 2};{descrição 3};...
'''

def salvar(banco_dados : dict[str, dict[str, list[list[str]]]]):
    #Excluir arquivos antigos
    if os.path.exists("./KANBANS"):
        for kanb in os.listdir("./KANBANS"):
            for cols in os.listdir(f"./KANBANS/{kanb}"):
                os.remove(f"./KANBANS/{kanb}/{cols}")
            os.removedirs(f"./KANBANS/{kanb}")
    
    for nome, colunas in banco_dados.items():
        
        #Criar pasta do kanban
        os.makedirs(f"KANBANS/{nome}")
        
        for coluna_name, lista in colunas.items():
            with open(f"KANBANS/{nome}/{coluna_name}.txt", "w", encoding= "utf-8") as file:
                for items in lista[:-1]:
                    file.write(";".join(items) + "\n")
                file.write(";".join(lista[-1]))
        

def carregar() -> dict[str, dict[str, list[list[str]]]]:
    database = {}
    for kanban in os.listdir("./KANBANS"):
        for coluna in os.listdir(f"./KANBANS/{kanban}"):
            with open(f"./KANBANS/{kanban}/{coluna}", "r", encoding= "utf-8") as file:
                componentes = [item[:-1].split(';') if "\n" in item else item.split(";") for item in file.readlines()]
            database[kanban] = {coluna[:-4] : componentes}
    return database


        

'''
    A Função Carregar precisa ser colocada na função criar_kanban
'''

'''
    A Função Salvar precisa ser colocada no botão salvar e quando um kanban for criado
'''

'''
    Colocar nas próximas funções, chamadas para quando iniciar carregar os dados:
        Função adicionar cartão
        Função Criar kanban
'''

'''
    Alterar o dicionario_de_cartoes para o formato novo
'''