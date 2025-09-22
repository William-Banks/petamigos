from src import db
from datetime import datetime

class Produto(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    preco = db.Column(db.Numeric(10,2), nullable=False)
    imagem = db.Column(db.String(255), nullable=True)
