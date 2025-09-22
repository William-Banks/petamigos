from src import ma
from src.models.usuario_model import Usuario
from marshmallow import fields

class UsuarioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Usuario
        load_instance = True

    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    email = fields.Email(required=True)
    senha = fields.Str(load_only=True, required=True)