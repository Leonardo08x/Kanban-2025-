'''
Tendo em vista que o nome do kanban será o nome da pasta/diretório,
cada kanban terá no mínimo 2 colunas,
cada coluna será um arquivo .txt dentro da pasta do kanban,
inicialmente as colunas não terão tarefas,
cada coluna poderá ter várias tarefas,
cada tarefa terá apenas uma pessoa responsável.


Modelo do bd:
    KANBANS/ -> pasta
        ID do kanban/ -> pasta kanban
            nome_kanban.txt -> nome do kanban
            COLUNAS/ -> pasta colunas
                coluna.txt
                    cor da coluna\n 
                    Tarefa1,Pessoa1\n
                    Tarefa2,Pessoa2\n
'''


'''
modelo memória volátil:
'''
'''
banco_dados : dict[str, dict[str, str | dict[str,str]]] = {
    "ID" : {
        "nome" : "Kanban_Teste",
        "Coluna 1" : {
            "cor" : "código hex ou o nome",
            "tarefa 1" : "pessoa 1",
            "tarefa 2" : "pessoa 2",
        } 
    },
    
    "2" : {
        "nome" : "Trabalho do Hidaka",
        "Front-end" : {
            "cor" : "green",
            "Fazer o site" : "Leo",
            "Documentar" : "Pt"
        },
        "Back-end" : {
            "cor" : "yellow",
            "Banco de dados" : "Gian",
            "Tratamento de erro" : "Reali"
        }
    }
}
'''



#Importar o componentes importantes
import os
import shutil #Discutir depois se pode usar shutil

#Criar a página principal que armazenará todos os kanbans
if not os.path.exists("./KANBANS"):   
    os.mkdir("./KANBANS")


#Ao criar o kanban, inicialmente só terá esses componentes:
'''
    Nome do kanban,
    Numero de colunas,
    cor das colunas
'''


def criar_kanban(banco_dados : dict[str, dict[str, str | dict[str,str]]], nome_kanban : str, num_coluna : int, cor_colunas : list[str]):
    '''
        Cria um kanban e adiciona no banco de dados volátil
        
        ### Parâmetros: 
        * banco_dados : banco de dados onde será adicionado o kanban recem criado
        * nome_kanban : nome que será atribuído ao kanban
        * num_coluna  : numero de colunas que existirá inicialmente no kanban
        * cor colunas : uma lista de cores que serão alocadas as colunas em ordem 
    '''
    
    #Criador de IDs para os kanbans (otimizado)
    status_create_id = False
    n = 1
    while not status_create_id:
        if str(n) not in banco_dados.keys():
            Id = str(n)
            status_create_id = True
        else:
            n += 1
    
    
    
    chaves = ["nome"]
    chaves.extend([f"coluna{x}" for x in range(1,num_coluna+1)])
    valores = [nome_kanban]
    valores.extend([{"cor" : cor_colunas[y]} for y in range(num_coluna)])
    banco_dados[Id] = dict(zip(chaves,valores))


def excluir_kanban(banco_dados : dict[str, dict[str, str | dict[str,str]]], Id: str):
    '''
        Exclui o Id de todos os banco de dados
    '''
    banco_dados.pop(Id, None)
    shutil.rmtree(f"./KANBANS/{Id}")


def salvar_kanban(banco_dados : dict[str, dict[str, str | dict[str,str]]], Id : str):
    '''
        Salva o banco de dados volátil
    '''
    
    kanban = banco_dados[Id]

    if not os.path.exists(f"./KANBANS/{Id}"):
        os.mkdir(f"./KANBANS/{Id}")
    
    with open(f"./KANBANS/{Id}/nome_kanban.txt", "w", encoding= "utf-8") as file:
        file.write(kanban["nome"])
    
    
    #Caso não existe cria, se existir exclua todos os arquivos antigos
    if not os.path.exists(f"./KANBANS/{Id}/COLUNAS"):
        os.mkdir(f"./KANBANS/{Id}/COLUNAS")
    else:
        for arq in os.listdir(f"./KANBANS/{Id}/COLUNAS"):
            os.remove(f"./KANBANS/{Id}/COLUNAS/{arq}")
    
    
    for coluna_nome,coluna_conteudo in list(kanban.items())[1:]:
                    
        with open(f"./KANBANS/{Id}/COLUNAS/{coluna_nome}.txt", "w", encoding= "utf-8") as arquivo:
            arquivo.write(f"{coluna_conteudo["cor"]}\n")
            for tarefa,pessoa in list(coluna_conteudo.items())[1:]:
                arquivo.write(f'{tarefa},{pessoa}\n')
        
    
def carregar_kanban():
    '''
        Ler os arquivo e retorna um banco de dados volátil
    '''
    database = {}
    
    for Id in os.listdir("./KANBANS"):
        database[Id] = {}
        
        with open(f"KANBANS/{Id}/nome_kanban.txt", "r", encoding= "utf-8") as file:
            database[Id]["nome"] = file.read()
        
        
        for coluna in os.listdir(f"./KANBANS/{Id}/COLUNAS"):
            
            with open(f"KANBANS/{Id}/COLUNAS/{coluna}", "r", encoding= "utf-8") as arquivo:
                linhas = [item.split(",") for item in arquivo.read().split("\n")]
                
                #usamos um slice [:-4] para retirar a extensão .txt
                database[Id][coluna[:-4]] = {"cor" : linhas[0][0]}
                
                #A primeira linha retorna a cor da coluna e a última linha é vazia por conta do \n final, então precisa excluir essas linhas da iteração
                for tarefa_coluna in linhas[1:-1]:
                    database[Id][coluna[:-4]][tarefa_coluna[0]] = tarefa_coluna[1]
        
    return database
            

def editar_kanban(banco_dados : dict[str, dict[str, str | dict[str,str]]], Id : str, nome_kanban : str, colunas : list[str], cor_colunas : list[str], tarefas : list[list[str]], pessoas : list[list[str]]):
    '''
        Altera o Banco de dados volátil
        
        #### Parâmetros:
        * banco_dados : banco de dados volátil
        * Id : id do kanban
        * colunas : uma lista contendo o nome das colunas
        * cor_colunas : uma lista contendo as cores da coluna ordenado pelo índice
        * tarefas : uma lista de lista onde cada lista está relacionado a coluna pelo índice e dentro de cada lista possui as tarefas relacionas para aquela coluna
        * pessoas : uma lista de listas onde cada lista está reacionado a coluna pelo índice e dentro de cada lista possui pessoas que se relacionam com as tarefas pelo índice
        
    '''
    banco_dados[Id] = {}
    
    banco_dados[Id]["nome"] = nome_kanban
    
    for column, column_color, lista_tarefa, list_pessoa in zip(colunas, cor_colunas, tarefas, pessoas):
        banco_dados[Id][column] = {"cor" : column_color}
        
        for tarefa, pessoa in zip(lista_tarefa, list_pessoa):
            banco_dados[Id][column][tarefa] = pessoa

