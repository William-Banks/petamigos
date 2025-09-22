from src.models.comentario_model import Comentario
from src import db
from src.schemas.comentario_schema import ComentarioSchema

class ComentarioService:
    def __init__(self):
        self.schema = ComentarioSchema()
        self.schema_many = ComentarioSchema(many=True)

    def criar_comentario(self, data):
        comentario = Comentario(
            conteudo=data.get("conteudo"),
            usuario_id=data.get("usuario_id"),
            post_id=data.get("post_id")
        )
        db.session.add(comentario)
        db.session.commit()
        return self.schema.dump(comentario)

    def listar_comentarios(self):
        comentarios = Comentario.query.all()
        return self.schema_many.dump(comentarios)

    def buscar_por_id(self, comentario_id):
        comentario = Comentario.query.get(comentario_id)
        if not comentario:
            return None
        return self.schema.dump(comentario)

    def atualizar_comentario(self, comentario_id, data):
        comentario = Comentario.query.get(comentario_id)
        if not comentario:
            return None
        comentario.conteudo = data.get("conteudo", comentario.conteudo)
        db.session.commit()
        return self.schema.dump(comentario)

    def deletar_comentario(self, comentario_id):
        comentario = Comentario.query.get(comentario_id)
        if not comentario:
            return False
        db.session.delete(comentario)
        db.session.commit()
        return True
