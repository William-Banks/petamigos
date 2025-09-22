from src import ma
from src.models.produto_model import Produto
from marshmallow import fields

class ProdutoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Produto
        load_instance = True

    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True)
    descricao = fields.Str()
    preco = fields.Decimal(required=True, as_string=True)
    imagem = fields.Str()