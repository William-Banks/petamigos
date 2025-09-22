from src.models.curtida_model import Curtida
from src import db
from src.schemas.curtida_schema import CurtidaSchema
from sqlalchemy.exc import IntegrityError

class CurtidaService:
    def __init__(self):
        self.schema = CurtidaSchema()
        self.schema_many = CurtidaSchema(many=True)

    def criar_curtida(self, data):
        curtida = Curtida(
            usuario_id=data.get("usuario_id"),
            post_id=data.get("post_id")
        )
        db.session.add(curtida)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Usuário já curtiu esse post.")
        return self.schema.dump(curtida)

    def listar_curtidas(self):
        curtidas = Curtida.query.all()
        return self.schema_many.dump(curtidas)

    def buscar_por_id(self, curtida_id):
        curtida = Curtida.query.get(curtida_id)
        if not curtida:
            return None
        return self.schema.dump(curtida)

    def deletar_curtida(self, curtida_id):
        curtida = Curtida.query.get(curtida_id)
        if not curtida:
            return False
        db.session.delete(curtida)
        db.session.commit()
        return True
