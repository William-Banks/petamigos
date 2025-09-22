from src.models.post_model import Post
from src import db
from src.schemas.post_schema import PostSchema

class PostService:
    def __init__(self):
        self.schema = PostSchema()
        self.schema_many = PostSchema(many=True)

    def criar_post(self, data):
        post = Post(
            tipo=data.get("tipo"),
            referencia_id=data.get("referencia_id"),
            titulo=data.get("titulo"),
            descricao=data.get("descricao"),
            imagem=data.get("imagem")
        )
        db.session.add(post)
        db.session.commit()
        return self.schema.dump(post)

    def listar_posts(self):
        posts = Post.query.all()
        return self.schema_many.dump(posts)

    def buscar_por_id(self, post_id):
        post = Post.query.get(post_id)
        if not post:
            return None
        return self.schema.dump(post)

    def atualizar_post(self, post_id, data):
        post = Post.query.get(post_id)
        if not post:
            return None
        post.tipo = data.get("tipo", post.tipo)
        post.referencia_id = data.get("referencia_id", post.referencia_id)
        post.titulo = data.get("titulo", post.titulo)
        post.descricao = data.get("descricao", post.descricao)
        post.imagem = data.get("imagem", post.imagem)
        db.session.commit()
        return self.schema.dump(post)

    def deletar_post(self, post_id):
        post = Post.query.get(post_id)
        if not post:
            return False
        db.session.delete(post)
        db.session.commit()
        return True
