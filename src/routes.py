from flask import Blueprint, request, jsonify, render_template
from flask import redirect, url_for
import os

from src.services.usuario_service import UsuarioService
from src.services.pet_service import PetService
from src.services.produto_service import ProdutoService
from src.services.post_service import PostService
from src.services.comentario_service import ComentarioService
from src.services.curtida_service import CurtidaService

main_bp = Blueprint("main", __name__)

usuario_service = UsuarioService()
pet_service = PetService()
produto_service = ProdutoService()
post_service = PostService()
comentario_service = ComentarioService()
curtida_service = CurtidaService()

# ===== Rotas para páginas HTML =====
@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/login")
def login():
    return render_template("login.html")

# ===== Rotas Usuario =====
@main_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = usuario_service.listar_usuarios()
    return jsonify(usuarios), 200

@main_bp.route("/usuarios", methods=["POST"])
def criar_usuario():
    data = request.get_json()
    try:
        usuario = usuario_service.criar_usuario(data)
        return jsonify(usuario), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@main_bp.route("/login", methods=["POST"])
def login_post():
    data = request.get_json()
    usuario = usuario_service.autenticar(data.get("email"), data.get("senha"))
    if usuario:
        return jsonify(usuario), 200
    else:
        return jsonify({"erro": "Credenciais inválidas"}), 401

# ===== Rotas Pet =====
@main_bp.route("/pets", methods=["GET"])
def listar_pets():
    pets = pet_service.listar_pets()
    return jsonify(pets), 200

@main_bp.route("/pets/<int:pet_id>", methods=["GET"])
def buscar_pet(pet_id):
    pet = pet_service.buscar_por_id(pet_id)
    if pet:
        return jsonify(pet), 200
    return jsonify({"erro": "Pet não encontrado"}), 404

@main_bp.route("/pets", methods=["POST"])
def criar_pet():
    data = request.get_json()
    pet = pet_service.criar_pet(data)
    return jsonify(pet), 201

@main_bp.route("/pets/<int:pet_id>", methods=["PUT"])
def atualizar_pet(pet_id):
    data = request.get_json()
    pet = pet_service.atualizar_pet(pet_id, data)
    if pet:
        return jsonify(pet), 200
    return jsonify({"erro": "Pet não encontrado"}), 404

@main_bp.route("/pets/<int:pet_id>", methods=["DELETE"])
def deletar_pet(pet_id):
    sucesso = pet_service.deletar_pet(pet_id)
    if sucesso:
        return jsonify({}), 204
    return jsonify({"erro": "Pet não encontrado"}), 404

# ===== Rotas Produto =====
@main_bp.route("/produtos", methods=["GET"])
def listar_produtos():
    produtos = produto_service.listar_produtos()
    return jsonify(produtos), 200

@main_bp.route("/produtos/<int:produto_id>", methods=["GET"])
def buscar_produto(produto_id):
    produto = produto_service.buscar_por_id(produto_id)
    if produto:
        return jsonify(produto), 200
    return jsonify({"erro": "Produto não encontrado"}), 404

@main_bp.route("/produtos", methods=["POST"])
def criar_produto():
    data = request.get_json()
    produto = produto_service.criar_produto(data)
    return jsonify(produto), 201

@main_bp.route("/produtos/<int:produto_id>", methods=["PUT"])
def atualizar_produto(produto_id):
    data = request.get_json()
    produto = produto_service.atualizar_produto(produto_id, data)
    if produto:
        return jsonify(produto), 200
    return jsonify({"erro": "Produto não encontrado"}), 404

@main_bp.route("/produtos/<int:produto_id>", methods=["DELETE"])
def deletar_produto(produto_id):
    sucesso = produto_service.deletar_produto(produto_id)
    if sucesso:
        return jsonify({}), 204
    return jsonify({"erro": "Produto não encontrado"}), 404

# ===== Rotas Post =====
@main_bp.route("/posts", methods=["GET"])
def listar_posts():
    posts = post_service.listar_posts()
    return jsonify(posts), 200

@main_bp.route("/posts/<int:post_id>", methods=["GET"])
def buscar_post(post_id):
    post = post_service.buscar_por_id(post_id)
    if post:
        return jsonify(post), 200
    return jsonify({"erro": "Post não encontrado"}), 404

@main_bp.route("/posts", methods=["POST"])
def criar_post():
    data = request.get_json()
    post = post_service.criar_post(data)
    return jsonify(post), 201

@main_bp.route("/posts/<int:post_id>", methods=["PUT"])
def atualizar_post(post_id):
    data = request.get_json()
    post = post_service.atualizar_post(post_id, data)
    if post:
        return jsonify(post), 200
    return jsonify({"erro": "Post não encontrado"}), 404

@main_bp.route("/posts/<int:post_id>", methods=["DELETE"])
def deletar_post(post_id):
    sucesso = post_service.deletar_post(post_id)
    if sucesso:
        return jsonify({}), 204
    return jsonify({"erro": "Post não encontrado"}), 404

# ===== Rotas Comentario =====
@main_bp.route("/comentarios", methods=["GET"])
def listar_comentarios():
    comentarios = comentario_service.listar_comentarios()
    return jsonify(comentarios), 200

@main_bp.route("/comentarios/<int:comentario_id>", methods=["GET"])
def buscar_comentario(comentario_id):
    comentario = comentario_service.buscar_por_id(comentario_id)
    if comentario:
        return jsonify(comentario), 200
    return jsonify({"erro": "Comentário não encontrado"}), 404

@main_bp.route("/comentarios", methods=["POST"])
def criar_comentario():
    data = request.get_json()
    comentario = comentario_service.criar_comentario(data)
    return jsonify(comentario), 201

@main_bp.route("/comentarios/<int:comentario_id>", methods=["PUT"])
def atualizar_comentario(comentario_id):
    data = request.get_json()
    comentario = comentario_service.atualizar_comentario(comentario_id, data)
    if comentario:
        return jsonify(comentario), 200
    return jsonify({"erro": "Comentário não encontrado"}), 404

@main_bp.route("/comentarios/<int:comentario_id>", methods=["DELETE"])
def deletar_comentario(comentario_id):
    sucesso = comentario_service.deletar_comentario(comentario_id)
    if sucesso:
        return jsonify({}), 204
    return jsonify({"erro": "Comentário não encontrado"}), 404

# ===== Rotas Curtida =====
@main_bp.route("/curtidas", methods=["GET"])
def listar_curtidas():
    curtidas = curtida_service.listar_curtidas()
    return jsonify(curtidas), 200

@main_bp.route("/curtidas/<int:curtida_id>", methods=["GET"])
def buscar_curtida(curtida_id):
    curtida = curtida_service.buscar_por_id(curtida_id)
    if curtida:
        return jsonify(curtida), 200
    return jsonify({"erro": "Curtida não encontrada"}), 404

@main_bp.route("/curtidas", methods=["POST"])
def criar_curtida():
    data = request.get_json()
    try:
        curtida = curtida_service.criar_curtida(data)
        return jsonify(curtida), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@main_bp.route("/curtidas/<int:curtida_id>", methods=["DELETE"])
def deletar_curtida(curtida_id):
    sucesso = curtida_service.deletar_curtida(curtida_id)
    if sucesso:
        return jsonify({}), 204
    return jsonify({"erro": "Curtida não encontrada"}), 404

@main_bp.route("/novo-post", methods=["GET"])
def formulario_post():
    return render_template("novo_post.html")

@main_bp.route("/novo-post", methods=["POST"])
def criar_post_manual():
    data = {
        "tipo": request.form.get("tipo"),
        "titulo": request.form.get("titulo"),
        "descricao": request.form.get("descricao"),
        "imagem": request.form.get("imagem"),
        "referencia_id": request.form.get("referencia_id")  # cuidado com isso
    }

    try:
        novo_post = post_service.criar_post(data)
        return redirect("/")
    except Exception as e:
        return f"Erro ao criar post: {e}", 400