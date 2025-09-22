from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configurações do app - ajuste conforme seu .env ou config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///petamigo.db'  # Exemplo, troque pelo seu banco
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'sua-chave-secreta-aqui'  # coloque uma variável de ambiente real

    # Inicializa extensões
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    from src.routes import main_bp
    app.register_blueprint(main_bp)

    return app
