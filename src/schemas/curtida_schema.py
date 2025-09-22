from src import ma
from src.models.curtida_model import Curtida
from marshmallow import fields

class CurtidaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Curtida
        load_instance = True

    id = fields.Int(dump_only=True)
    usuario_id = fields.Int(required=True)
    post_id = fields.Int(required=True)
    criado_em = fields.DateTime(dump_only=True)
