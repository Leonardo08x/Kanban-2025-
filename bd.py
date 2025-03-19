bd = [
    {
        'nome': 'kanban 1',
        'colunas': [
            {
                'nome': 'coluna 1',
                'cor': 'vermelha',
                'tarefas': [
                    ('responsavel', 'tarefa 1'),
                    ('responsavel', 'tarefa 2'),
                ],
            },
            {
                'nome': 'coluna 2',
                'cor': 'laranja',
                'tarefas': [
                        ('junior', 'catar manga'),
                        ('alessandro', 'ajudar o junior'),
                ],
            }
        ]
    },
    {
        'nome': 'kanban 2',
        'colunas': [
            {
                'nome': 'coluna 1',
                'cor': 'vermelha',
                'tarefas': [
                    ('responsavel', 'tarefa 1'),
                ],
            },
            {
                'nome': 'coluna 2',
                'cor': 'laranja',
                'tarefas': [
                    ('leonardo', 'designer'),
                    ('gian', 'banco de dados'),
                    ('thiago', 'frontend'),
                ],
            }
        ]
    },
]


# bd -> list[dict[str, list[dict[str, list[tuple[str, str]]]]