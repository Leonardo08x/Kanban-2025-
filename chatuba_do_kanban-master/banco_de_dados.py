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


def criar_kanban(banco_dados, nome_kanban : str, num_coluna : int, cor_colunas : list[str]):
    #Discutir sobre o código de criar ID automticamente que o Gian possui
    id = str(max([int(x) for x in banco_dados.keys()])+1)
    
    chaves = ["nome"]
    chaves.extend([f"coluna{x}" for x in range(1,num_coluna+1)])
    valores = [nome_kanban]
    valores.extend([{"cor" : cor_colunas[y]} for y in range(num_coluna)])
    
    banco_dados[id] = dict(zip(chaves,valores))


def excluir_kanban(banco_dados, Id: str):
    banco_dados.pop(Id, None)
    
    shutil.rmtree(f"./KANBANS/{Id}")


def salvar_kanban(banco_dados, Id : str):
    kanban = banco_dados[Id]

    if not os.path.exists(f"./KANBANS/{Id}"):
        os.mkdir(f"./KANBANS/{Id}")
    
    with open(f"./KANBANS/{Id}/nome_kanban.txt", "w", encoding= "utf-8") as file:
        file.write(kanban["nome"])
    
    lista = list(kanban.items())
    
    if not os.path.exists(f"./KANBANS/{Id}/COLUNAS"):
        os.mkdir(f"./KANBANS/{Id}/COLUNAS")
    else:
        for arq in os.listdir(f"./KANBANS/{Id}/COLUNAS"):
            os.remove(f"./KANBANS/{Id}/COLUNAS/{arq}")
    
    for coluna_nome,coluna_conteudo in lista[1:]:
        lis = list(coluna_conteudo.items())
                    
        with open(f"./KANBANS/{Id}/COLUNAS/{coluna_nome}.txt", "w", encoding= "utf-8") as arquivo:
            arquivo.write(f"{coluna_conteudo["cor"]}\n")
            for tarefa,pessoa in lis[1:]:
                arquivo.write(f'{tarefa},{pessoa}\n')
        
    
def carregar_kanban():
    database = {}
    
    for Id in os.listdir("./KANBANS"):
        database[Id] = {}
        
        with open(f"KANBANS/{Id}/nome_kanban.txt", "r", encoding= "utf-8") as file:
            database[Id]["nome"] = file.read()
        
        for coluna in os.listdir(f"./KANBANS/{Id}/COLUNAS"):
            
            with open(f"KANBANS/{Id}/COLUNAS/{coluna}", "r", encoding= "utf-8") as arquivo:
                linhas = [item.split(",") for item in arquivo.read().split("\n")]
                
                database[Id][coluna[:-4]] = {"cor" : linhas[0][0]}
                
                for tarefa_coluna in linhas[1:-1]:
                    database[Id][coluna[:-4]][tarefa_coluna[0]] = tarefa_coluna[1]
        
    return database
            

def editar_kanban(banco_dados, Id:str, nome_kanban:str, colunas:list[str], cor_colunas:list[str], tarefas:list[list[str]], pessoas:list[list[str]]):
    banco_dados[Id] = {}
    
    banco_dados[Id]["nome"] = nome_kanban
    
    for column, column_color, lista_tarefa, list_pessoa in zip(colunas, cor_colunas, tarefas, pessoas):
        banco_dados[Id][column] = {"cor" : column_color}
        
        for tarefa, pessoa in zip(lista_tarefa, list_pessoa):
            banco_dados[Id][column][tarefa] = pessoa

