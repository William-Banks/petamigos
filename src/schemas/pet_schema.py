from src import ma
from src.models.pet_model import Pet
from marshmallow import fields

class PetSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Pet
        load_instance = True

    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    descricao = fields.Str()
    imagem = fields.Str()