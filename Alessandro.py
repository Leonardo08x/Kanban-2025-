import os, re

#Exemplo da variável do banco de dados
banco_dados = [
    {
        "nome" : "{nome_do_kanban}",
        "ID" : "{ID_único_do_kanban}",
        "colunas" : [
            {
                "nome" : "{nome_da_coluna}",
                "cor" : "{cor_da_coluna}",
                "ID" : "{ID_unico_da_coluna}",
                "tarefas" : [
                    ("{responsavel}","{tarefa}")
                ]
            }
        ]
    }
]


#############################      FUNÇÕES AUXILIARES       ##################################


def criador_ID(caminho):
    '''
        Cria um ID único para cada kaban ou coluna
    '''
    #Recupero todos os IDs existente na pasta analisada
    lista = [int(re.match(r"\d+", item).group()) for item in os.listdir(caminho)]
    
    #Verifico se entre o menor ID(0) e o maior ID existe lacuna
    #Se existir, os novos IDs cobrirão essas lacunas
    #Se não houver, ele pega o maior ID e adiciona +1
    if len(lista) == 0:
        lista = [-1]
    for Id in range(max(lista)):
        if Id not in lista:
            return str(Id)
    return str(max(lista)+1)




def excluir_tudo():
    '''
            Função que exclui todos os kanbans
            
            Criado para evitar duplicadas de kanbans sem a intenção do usuário
            
            Caso queira, pode criar um botão para excluir todos os kanbans exitentes
    '''
    
    #Verifico se existe a pasta dos kanbans, evitando erro
    if not os.path.exists("KANBANS"):
        return None
    
    #Itero todos os kanbans e seus arquivos e excluo tudo
    for pasta in os.listdir(f"KANBANS"):
        for arquivo in os.listdir(f"KANBANS/{pasta}"):
            os.remove(f"KANBANS/{pasta}/{arquivo}")
        os.removedirs(f"KANBANS/{pasta}")


################################     DATABASE CRUD     ####################################


def salvar(banco_dados : list[dict[str, str | list[dict[str, str | list[tuple[str]]]]]]):
    '''
        Função que salvao banco de dados
        
        Só deve ser usado quando um novo banco de dados for criado, não estando incluso a 
        função de excluir ou editar
    '''
    
    #Excluo tudo, para evitar duplicadas
    excluir_tudo()
    
    #Se a pasta KANBANS não existir, cria ela
    if not os.path.exists("KANBANS"):
        os.mkdir("KANBANS")
    
    #itero os dicionarios
    for kanban in banco_dados:
        
        
        #Crio as pastas com o nome de cada kanban e seu respectivo IDs.
        os.mkdir(f"./KANBANS/{kanban["ID"]}--{kanban["nome"]}")
    
        #itero a lista de colunas
        for coluna in kanban["colunas"]:
            
            #Crio a arquivo txt referente ao nome de cada coluna e seus respectivos IDs
            with open(f"./KANBANS/{kanban["ID"]}--{kanban["nome"]}/{coluna["ID"]}--{coluna["nome"]}.txt", "w", encoding= "utf-8") as file:
                
                #escrevo na primeira linha a cor da coluna
                file.write(coluna["cor"] + "\n")
                
                #As demais linhas serão no formato: {pessoa};{tarefa}\n
                for tarefa in coluna["tarefas"][:-1]:
                    file.write(";".join(tarefa) + "\n")
                file.write(";".join(coluna["tarefas"][-1]))




def carregar() -> list[dict[str, str | list[dict[str, str | list[tuple[str]]]]]] :
    '''
        Função que retorna um banco de dados volátil baseado no banco de dados permanente
    '''
    
    #Crio o banco de dados vazio
    database = []
    
    #itero todos os kanbans na pasta KANBANS
    for kanban in os.listdir("KANBANS"):
        
        #Crio o dicionário do kanban, alocando o nome e o ID
        dicionario = {
            "nome" : re.search(r"(?<=--).*$", kanban).group(),
            "ID" : re.match(r"\d+", kanban).group()
        }
        
        #Crio a lista das colunas vazia
        coluna = []
        
        #itero os arquivos referente as colunas dentro da pasta do kanban
        for arquivo in os.listdir(f"KANBANS/{kanban}"):
            
            #Crio o dicionario referente a coluna, alocando o nome
            dicio = {
                "nome" : re.search(r"(?<=--).*(?=\.)", arquivo).group(),
                "ID" : re.match(r"\d+",arquivo).group()
            }
            
            #Abro os arquivos para recuperar suas linhas
            with open(f"KANBANS/{kanban}/{arquivo}", "r", encoding= "utf-8") as file:
                linhas = [item[:-1] if "\n" in item else item for item in file.readlines()]
            
            #defino no dicionario da coluna a chave cor com o valor da primeira linha
            dicio["cor"] = linhas[0]
            
            #defino no dicionario da coluna a chave tarefas com o valor uma lista vazia
            dicio["tarefas"] = []
            
            #itero as outras linhas do arquivo que são referentes a atividades e seus responsáveis
            #e colocos dentro da lista de tarefas
            for tarefa in linhas[1:]:
                dicio["tarefas"].append(tuple(tarefa.split(";")))
            
            #Adiciona o dicionario referente a coluna dentro da lista de coluna
            coluna.append(dicio)
        
        #defino no dicionario do kanban a chave colunas com o valor a lista de colunas
        dicionario["colunas"] = coluna
        
        #Adiciono o dicionario do kanban da lista de kanbans
        database.append(dicionario)
    
    #Retorna a lista de kanbans
    return database




def excluir(Id : float, banco_dados:list, delete = True):
    '''
        exclui um kanban baseado no seu ID
    '''
    
    #itero todos os kanbans da pasta KANBANS e procuro um ID específico
    for diretorio in os.listdir("KANBANS"):
        if Id == re.match(r"\d+", diretorio).group():
            
            #Se eu encontrar o ID específicado, eu excluo a pasta com todos os arquivos dentro
            for file in os.listdir(f"KANBANS/{diretorio}"):
                os.remove(file)
            os.removedirs(f"KANBANS/{diretorio}")
            break
    
    #Essa verificação é apenas para uso futuro
    if delete:
        for kanban in banco_dados:
            if kanban["ID"] == "ID":
                
                #Coloquei un return para parar a função quando ele remove o kanban,evitando gastos desnecessários
                return banco_dados.remove(kanban)
                     



def editar(Id : int, banco_dados: list, novo_kanban: dict):
    '''
        Edita o kanban selecionado pelo processo:
        
        Verifica o aquivo correspondente e exclui o antigo.
        Depois, adiciona o novo kanban tanto ao banco de dados volátil quanto nos arquivos
    '''
    
    #exclui o antigo kanban, sem o retirar do banco de dados
    excluir(Id, banco_dados, delete= False)
    
    #adiciona o novo kanban ao banco de dados volátil no índice do antigo
    for index, kanban in enumerate(banco_dados):
        if kanban["ID"] == Id:
            banco_dados[index] = novo_kanban
            break
    
    #A partir daqui é igual ao final da função salvar
    #Note que o ID não se alterou, muito importante ressaltar
    
    #Crio a pasta do kanban com seu nome e seu ID
    os.mkdir(f"./KANBANS/{Id}--{novo_kanban["nome"]}")

    #itero a lista de colunas
    for coluna in novo_kanban["colunas"]:
        
        #Crio um novo ID para as colunas, pois evita erro caso haja alteração no números de colunas
        ddi = criador_ID(f"./KANBANS/{Id}--{novo_kanban["nome"]}")
        
        #Crio a arquivo txt referente ao nome de cada coluna e seus respectivos IDs 
        with open(f"./KANBANS/{Id}--{novo_kanban["nome"]}/{ddi}--{coluna["nome"]}.txt", 
                "w", encoding= "utf-8") as file:
            
            #escrevo na primeira linha a cor da coluna
            file.write(coluna["cor"] + "\n")
            
            #As demais linhas serão no formato: {pessoa};{tarefa}\n
            for tarefa in coluna["tarefas"][:-1]:
                file.write(";".join(tarefa) + "\n")
            file.write(";".join(coluna["tarefas"][-1]))