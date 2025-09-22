from src import ma
from src.models.post_model import Post
from marshmallow import fields
from src.schemas.comentario_schema import ComentarioSchema
from src.schemas.curtida_schema import CurtidaSchema

class PostSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Post
        load_instance = True

    id = fields.Int(dump_only=True)
    tipo = fields.Str(required=True)
    referencia_id = fields.Int(required=True)
    titulo = fields.Str(required=True)
    descricao = fields.Str()
    imagem = fields.Str()
    criado_em = fields.DateTime(dump_only=True)

    comentarios = fields.List(fields.Nested(ComentarioSchema), dump_only=True)
    curtidas = fields.List(fields.Nested(CurtidaSchema), dump_only=True)
