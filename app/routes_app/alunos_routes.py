from flask import Blueprint, request, jsonify
from ..models import db, Aluno

alunos_bp = Blueprint("alunos", __name__)

@alunos_bp.route("/alunos", methods=["GET"])
def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify([
        {"id": a.id_aluno, "nome": a.nome_aluno, "encodings": a.encodings_aluno}
        for a in alunos
    ])

@alunos_bp.route("/alunos/<int:id>", methods=["GET"])
def obter_aluno(id):
    aluno  = Aluno.query.get_or_404(id)
    return jsonify({"id": aluno.id_aluno, "nome": aluno.nome_aluno, "encodings": aluno.encodings_aluno})

@alunos_bp.route("/alunos", methods=["POST"])
def criar_aluno():
    data = request.get_json()
    novo_aluno = Aluno(
        nome_aluno=data["nome_aluno"],
        encodings_aluno=data["encodings_aluno"]
    )
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify({"mensagem": "Aluno criado com sucesso!"}), 201

@alunos_bp.route("/alunos/<int:id>", methods=["PUT"])
def atualizar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    data = request.get_json()
    aluno.nome_aluno = data.get("nome_aluno", aluno.nome_aluno)
    aluno.encodings_aluno = data.get("encodings_aluno", aluno.encodings_aluno)
    db.session.commit()
    return jsonify({"mensagem": "Aluno atualizado com sucesso!"})

@alunos_bp.route("/alunos/<int:id>", methods=["DELETE"])
def deletar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    return jsonify({"mensagem": "Aluno deletado com sucesso!"})