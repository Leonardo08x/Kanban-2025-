bd = [
    {
        'nome': 'kanban 1',
        'ID': '0',
        'colunas': [
            {
                'nome': 'coluna 1',
                'cor': 'vermelha',
                'ID': '0',
                'tarefas': [
                    ('responsavel', 'tarefa 1'),
                    ('responsavel', 'tarefa 2'),
                ],
            },
            {
                'nome': 'coluna 2',
                'cor': 'laranja',
                'ID': '1',
                'tarefas': [
                        ('junior', 'catar manga'),
                        ('alessandro', 'ajudar o junior'),
                ],
            }
        ]
    },
    {
        'nome': 'kanban 2',
        'ID': '1',
        'colunas': [
            {
                'nome': 'coluna 1',
                'cor': 'vermelha',
                'ID': '0',
                'tarefas': [
                    ('responsavel', 'tarefa 1'),
                ],
            },
            {
                'nome': 'coluna 2',
                'cor': 'laranja',
                'ID': '1',
                'tarefas': [
                    ('leonardo', 'designer'),
                    ('gian', 'banco de dados'),
                    ('thiago', 'frontend'),
                ],
            }
        ]
    },
]

def carregar_bd() -> list[dict[str, str | list[dict[str, str |list[tuple[str, str]]]]]]:
    return bd