from src.models.usuario_model import Usuario
from src import db
from werkzeug.security import generate_password_hash, check_password_hash
from src.schemas.usuario_schema import UsuarioSchema

class UsuarioService:
    def __init__(self):
        self.schema = UsuarioSchema()

    def criar_usuario(self, data):
        # Espera dicionário com keys: nome, email, senha
        # Verifica se email já existe
        if Usuario.query.filter_by(email=data.get("email")).first():
            raise ValueError("Email já cadastrado")

        usuario = Usuario(
            nome=data.get("nome"),
            email=data.get("email")
        )
        # Armazena a senha com hash
        usuario.senha = generate_password_hash(data.get("senha"))

        db.session.add(usuario)
        db.session.commit()
        return self.schema.dump(usuario)

    def autenticar(self, email, senha):
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and check_password_hash(usuario.senha, senha):
            return self.schema.dump(usuario)
        return None

    def buscar_por_id(self, usuario_id):
        usuario = Usuario.query.get(usuario_id)
        if not usuario:
            return None
        return self.schema.dump(usuario)

    def listar_usuarios(self):
        usuarios = Usuario.query.all()
        return UsuarioSchema(many=True).dump(usuarios)