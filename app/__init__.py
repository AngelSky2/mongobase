from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/catalogo_recetas"

    mongo.init_app(app)
    CORS(app)

    # Importar todos los blueprints
    from .routes.usuario_routes import usuario_bp
    from .routes.ingredientes import ingredientes_bp
    from .routes.recetas import recetas_bp

    # Registrar todos los blueprints
    app.register_blueprint(usuario_bp)
    app.register_blueprint(ingredientes_bp)
    app.register_blueprint(recetas_bp)

    return app
