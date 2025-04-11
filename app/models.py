from . import db

class Teste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))