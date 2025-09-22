from src import ma
from src.models.comentario_model import Comentario
from marshmallow import fields

class ComentarioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Comentario
        load_instance = True

    id = fields.Int(dump_only=True)
    conteudo = fields.Str(required=True)
    data_criacao = fields.DateTime(dump_only=True)
    usuario_id = fields.Int(required=True)
    post_id = fields.Int(required=True)
