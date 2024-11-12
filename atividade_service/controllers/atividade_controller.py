from flask import Blueprint, jsonify, request
from models.atividade_model import AtividadeNotFound,listar_atividades,obter_atividade,adicionar_atividade,mudar_atividade,excluir_atividade
from clients.pessoa_service_client import PessoaServiceClient


atividade_bp = Blueprint('atividade_bp', __name__)


@atividade_bp.route('/', methods=['GET'])
def atividades():
    atividades = listar_atividades()
    return jsonify(atividades)


@atividade_bp.route('/<int:id_atividade>', methods=['GET'])
def atividade_id(id_atividade):
    try:
        atividade = obter_atividade(id_atividade)
        return jsonify(atividade)
    except AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404


@atividade_bp.route('/<int:id_atividade>/professor/<int:id_professor>', methods=['GET'])
def obter_atividade_para_professor(id_atividade, id_professor):
    try:
        atividade = obter_atividade(id_atividade)
        if not PessoaServiceClient.verificar_leciona(id_professor, atividade['id_disciplina']):
            atividade = atividade.copy()
            atividade.pop('respostas', None)
        return jsonify(atividade)
    except AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404


@atividade_bp.route('/', methods=['POST'])
def add_atividade():
    data = request.json
    adicionar_atividade(data)
    return listar_atividades(), 201


@atividade_bp.route('/<int:id_atividade>', methods=['PUT'])
def atualizar_atividade(id_atividade):
    data = request.json
    try:
        mudar_atividade(id_atividade, data)
        return obter_atividade(id_atividade), 200
    except AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404


@atividade_bp.route('/<int:id_atividade>', methods=['DELETE'])
def deletar_atividade(id_atividade):
    try:
        return excluir_atividade(id_atividade)
    except AtividadeNotFound:
        return jsonify({'erro': 'Atividade não encontrada'}), 404