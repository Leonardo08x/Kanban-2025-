# main_bd.py é o menu principal do programa, serve para testar as funções do bd.py e controle_bd.py

import controle_bd as con
import bd

while True:
    opcao = input("0 - Sair\n1 - Criar kanban\n2 - Deletar kanban\n3 - Visualizar kanban\n4 - Listar kanbans\n5 - Editar kanban\n\nEscolha: ")

    if opcao == '0':
        print('Saindo...')
        break

    elif opcao == '1':
        con.criar()

    elif opcao == '2':
        con.deletar()

    elif opcao == '3':
        con.visualizar()

    elif opcao == '4':
        con.listar()

    elif opcao == '5':
        con.editar()

    else:
        print('Opção inválida')

# Execute o código e teste as funções do bd.py e controle_bd.py