from src import db
from datetime import datetime

class Curtida(db.Model):
    __tablename__ = "curtidas"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (db.UniqueConstraint("usuario_id", "post_id", name="uq_usuario_post"),)
