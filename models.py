from database import db
from datetime import datetime

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

class Experiencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=True)

    destino = db.Column(db.String(100), nullable=False)
    dias = db.Column(db.Integer, nullable=False)
    pessoas = db.Column(db.Integer, nullable=False)

    gasto_planejado = db.Column(db.Float, nullable=False)
    gasto_real = db.Column(db.Float, nullable=False)

    tipo_viagem = db.Column(db.String(50), nullable=False)
    avaliacao = db.Column(db.Integer, nullable=False)

    comentario = db.Column(db.Text, nullable=False)
    dicas = db.Column(db.Text, nullable=True)
    itens_mala = db.Column(db.Text, nullable=True)

    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    experiencia_id = db.Column(db.Integer, db.ForeignKey("experiencia.id"), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=True)
    texto = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)