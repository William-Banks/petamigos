from src.models.produto_model import Produto
from src import db
from src.schemas.produto_schema import ProdutoSchema

class ProdutoService:
    def __init__(self):
        self.schema = ProdutoSchema()
        self.schema_many = ProdutoSchema(many=True)

    def criar_produto(self, data):
        produto = Produto(
            nome=data.get("nome"),
            descricao=data.get("descricao"),
            preco=data.get("preco"),
            imagem=data.get("imagem")
        )
        db.session.add(produto)
        db.session.commit()
        return self.schema.dump(produto)

    def listar_produtos(self):
        produtos = Produto.query.all()
        return self.schema_many.dump(produtos)

    def buscar_por_id(self, produto_id):
        produto = Produto.query.get(produto_id)
        if not produto:
            return None
        return self.schema.dump(produto)

    def atualizar_produto(self, produto_id, data):
        produto = Produto.query.get(produto_id)
        if not produto:
            return None
        produto.nome = data.get("nome", produto.nome)
        produto.descricao = data.get("descricao", produto.descricao)
        produto.preco = data.get("preco", produto.preco)
        produto.imagem = data.get("imagem", produto.imagem)
        db.session.commit()
        return self.schema.dump(produto)

    def deletar_produto(self, produto_id):
        produto = Produto.query.get(produto_id)
        if not produto:
            return False
        db.session.delete(produto)
        db.session.commit()
        return True
