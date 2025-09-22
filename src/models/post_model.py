from src import db
from datetime import datetime

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Enum("pet", "produto", name="tipo_post"), nullable=False)
    referencia_id = db.Column(db.Integer, nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    imagem = db.Column(db.String(255), nullable=True)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    comentarios = db.relationship("Comentario", backref="post", lazy=True, cascade="all, delete-orphan")
    curtidas = db.relationship("Curtida", backref="post", lazy=True, cascade="all, delete-orphan")
