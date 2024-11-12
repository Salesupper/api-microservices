atividades = [
    {
        'id_atividade': 1,
        'id_disciplina': 1,
        'enunciado': 'Crie um app de todo em Flask',
        'respostas': [
            {'id_aluno': 1, 'resposta': 'todo.py', 'nota': 9},
            {'id_aluno': 2, 'resposta': 'todo.zip.rar'},
            {'id_aluno': 4, 'resposta': 'todo.zip', 'nota': 10}
        ]
    },
    {
        'id_atividade': 2,
        'id_disciplina': 1,
        'enunciado': 'Crie um servidor que envia email em Flask',
        'respostas': [
            {'id_aluno': 4, 'resposta': 'email.zip', 'nota': 10}
        ]
    }
]


class AtividadeNotFound(Exception):
    pass


def listar_atividades():
    return atividades


def obter_atividade(id_atividade):
    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade:
            return atividade
    raise AtividadeNotFound


def adicionar_atividade(data):
    atividade = {
        'id_atividade': len(atividades) + 1,
        'id_disciplina': data['id_disciplina'],
        'enunciado': data['enunciado'],
        'respostas':[{
            'id_aluno': r['id_aluno'],
            'resposta': r['resposta'],
            'nota': r.get('nota') 
            }
            for r in data['respostas']
        ]
    }
    atividades.append(atividade)


def mudar_atividade(id_atividade,data):
    atividade = obter_atividade(id_atividade)
    att = {
        'id_atividade': id_atividade,
        'id_disciplina': data['id_disciplina'],
        'enunciado': data['enunciado'],
        'respostas':[{
            'id_aluno': r['id_aluno'],
            'resposta': r['resposta'],
            'nota': r['nota'] 
            }
            for r in data['respostas']
        ]
    }
    atividade.update(att)


def excluir_atividade(id_atividade):
    att = obter_atividade(id_atividade)
    atividades.remove(att)
    return {'mensagem': 'atividade removida'}
