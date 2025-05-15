from flask import Blueprint, request, jsonify
from ..models import db, Curso
from datetime import datetime

cursos_bp = Blueprint("cursos", __name__)

@cursos_bp.route("/cursos", methods=["GET"])
def listar_cursos():
    cursos = Curso.query.all()
    return jsonify([
        {
            "id": c.id_curso,
            "nome": c.nome_curso,
            "data_inicio": c.data_inicio_curso.isoformat(),
            "data_fim": c.data_fim_curso.isoformat(),
            "dias_semana": c.dias_semana_curso
        }
        for c in cursos
    ])

@cursos_bp.route("/cursos/<int:id>", methods=["GET"])
def obter_curso(id):
    curso = Curso.query.get_or_404(id)
    return jsonify({
        "id": curso.id_curso,
        "nome": curso.nome_curso,
        "data_inicio": curso.data_inicio_curso.isoformat(),
        "data_fim": curso.data_fim_curso.isoformat(),
        "dias_semana": curso.dias_semana_curso
    })

@cursos_bp.route("/cursos", methods=["POST"])
def criar_curso():
    data = request.get_json()

    novo_curso = Curso(
        nome_curso=data["nome_curso"],
        data_inicio_curso=datetime.strptime(data["data_inicio_curso"], "%Y-%m-%d").date(),
        data_fim_curso=datetime.strptime(data["data_fim_curso"], "%Y-%m-%d").date(),
        dias_semana_curso=data["dias_semana_curso"]
    )

    db.session.add(novo_curso)
    db.session.commit()
    return jsonify({"mensagem": "Curso criado com sucesso!"}), 201

@cursos_bp.route("/cursos/<int:id>", methods=["PUT"])
def atualizar_curso(id):
    curso = Curso.query.get_or_404(id)
    data = request.get_json()

    curso.nome_curso = data.get("nome_curso", curso.nome_curso)
    if "data_inicio_curso" in data:
        curso.data_inicio_curso = datetime.strptime(data["data_inicio_curso"], "%Y-%m-%d").date()
    if "data_fim_curso" in data:
        curso.data_fim_curso = datetime.strptime(data["data_fim_curso"], "%Y-%m-%d").date()
    if "dias_semana_curso" in data:
        curso.dias_semana_curso = data["dias_semana_curso"]

    db.session.commit()
    return jsonify({"mensagem": "Curso atualizado com sucesso!"})

@cursos_bp.route("/cursos/<int:id>", methods=["DELETE"])
def deletar_curso(id):
    curso = Curso.query.get_or_404(id)
    db.session.delete(curso)
    db.session.commit()
    return jsonify({"mensagem": "Curso deletado com sucesso!"})