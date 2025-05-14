from . import db
from sqlalchemy.dialects.postgresql import JSON
from datetime import date

class Aluno(db.Model):
    id_aluno = db.Column(db.Integer, primary_key=True)
    nome_aluno = db.Column(db.String(100), nullable=False)
    encodings_aluno = db.Column(JSON, nullable=False)

class Curso(db.Model):
    id_curso  = db.Column(db.Integer, primary_key=True)
    nome_curso = db.Column(db.String(100), nullable=False)
    data_inicio_curso = db.Column(db.Date, nullable=False)
    data_fim_curso = db.Column(db.Date, nullable=False)
    dias_semana_curso = db.Column(JSON, nullable=False)

class Matricula(db.Model):
    id_matricula = db.Column(db.Integer, primary_key=True)
    id_aluno_fk = db.Column(db.Integer, db.ForeignKey("aluno.id_aluno"), nullable=False)
    id_curso_fk = db.Column(db.Integer, db.ForeignKey("curso.id_curso"), nullable=False)
    aluno = db.relationship("Aluno", backref="matriculas")
    curso = db.relationship("Curso", backref="matriculas")

class Presenca(db.Model):
    id_presenca = db.Column(db.Integer, primary_key=True)
    data_presenca = db.Column(db.Date, nullable=False)
    status_presenca = db.Column(db.Boolean, nullable=False, default=False)
    id_aluno_fk = db.Column(db.Integer, db.ForeignKey("aluno.id_aluno"), nullable=False)
    id_curso_fk = db.Column(db.Integer, db.ForeignKey("curso.id_curso"), nullable=False)
    aluno = db.relationship("Aluno", backref="presencas")
    curso = db.relationship("Curso", backref="presencas")