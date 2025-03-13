'''
Tendo em vista que o nome do kanban será o nome da pasta/diretório,
cada kanban terá no mínimo 2 colunas,
cada coluna será um arquivo .txt dentro da pasta do kanban,
inicialmente as colunas não terão tarefas,
cada coluna poderá ter várias tarefas,
cada tarefa terá apenas uma pessoa responsável.


Modelo do bd:
    KANBANS/ -> pasta
        Nome do kanban/ -> pasta kanban
            COLUNAS/ -> pasta colunas
                coluna.txt
                    cor da coluna\n 
                    Tarefa1,Pessoa1\n
                    Tarefa2,Pessoa2\n
'''


'''
modelo memória volátil:    
    kanban = {
        "Nome_coluna" : {
            "Tarefa" : "Pessoa"
            },
        "Nome_coluna" : {
            "Tarefa" : "Pessoa"
            }
        }
'''





import os
from functools import reduce

if not os.path.exists("./KANBANS"):   
    os.mkdir("./KANBANS")

#Tela criar
    #Nome do kanban
, color: strdef criar(dir_name : str, num_colunas : int):
    if oreturn False
    dir_name}"):
        returf"./KANBANS/{dir_name}""
#tem um codigo nesse erro    
    for numero in range(num_colunas):
        with open(f"./KANBANS/{dir_name}/coluna{numero}.txt", "w", encoding= "utf-8") as file:
            file.write(color+"\n")./KANBANS/{}" False
    os.mkdir(f)

# excluir a pasta kanban    
def excluir(file_name):
    os.removedirs(f"./KANBANS/{file_name}")


# carregar o kanban do bd para uma variável volátil
def carregar(file_name : str):
    if not os.path.exists(f"./KANBANS/{file_name}"):
        for colunas in os.listdir()
    

    


# salvar o kanban da variável volátil para o bddef editar_kanban(kanban):
def editar_kanban(kanban):
    '''
    recebe os valores do kanban e tranforma em pastas e arquivos.txt
    '''
    pass

