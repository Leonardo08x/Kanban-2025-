# Gerenciamento de tarefas com Kanban
Inspiração: https://gallery.flet.dev/trolli/#/boards  
Requisitos:
 
## Tela de criação de Kanbans
Ao criar um Kanban, o usuário deve definir o nome do Kanban, a quantidade de colunas e os seus nomes.
Todos os campos são obrigatórios e cada Kanban deve ter pelo menos duas colunas.

## Tela de gerenciamento de Kanban
O usuário deve selecionar o Kanban que deseja gerenciar.
A tela de gerenciamento do Kanban é a sua tela principal.
Na listagem dos Kanbans, devem ter as ações para editar e deletar Kanbans.
A tela de edição é similar a tela e criação de Kanbans.
Nesta tela você deve ter uma ação para ir para a tela que permite a criação de um novo kanban.

## Tela do Kanban aberto
Criação de tarefa definindo o responsável pela tarefa
A tarefa sempre é criada na primeira coluna do Kanban
Nesta dela deve ser possível mover as tarefas entre as colunas do Kanban

## Tela de pesquisa
Esta tela deve possibilitar filtrar tarefas por responsável, por Kanban e por colunas.
O filtro do Kanban é por caixa de seleção. A caixa de seleção tem que ter a opção todos.
A coluna é uma caixa de seleção que só pode mostrar as colunas do Kanban selecionado. Se o Kanban selecionado for todos, então tem que mostrar todas as colunas. A opção todas tem que aparecer também.
O filtro para responsável é um campo de texto livre e a regra é por começar com o valor digitado.
O filtro por responsável deve desconsiderar letras maiúsculas a acentos.

O seu programa não pode ser volátil. Utilize manipulação de arquivos para criar um estratégia para salvar os Kanbans e as tarefas deles. Dica, fica mais fácil se você utilizar mais de um arquivo.
