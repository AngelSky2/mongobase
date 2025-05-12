from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

mongo= PyMongo()
def create_app():
    app=Flask(__name__)
    app.config["MONGO_URI"]="mongodb://localhost:27017/catalogo_recetas"

    mongo.init_app(app)
    CORS(app)
    from .routes.usuario_routes import usuario_bp

    app.register_blueprint(usuario_bp)
    return app