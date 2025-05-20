from flask import Flask
from flask_pymongo import PyMongo
mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/catalogo_recetas"
    mongo.init_app(app)

    from .routes.usuario_routes import usuario_bp
    from .routes.ingredientes import ingredientes_bp
    from .routes.recetas import recetas_bp
    from .routes.views import views_bp

    app.register_blueprint(usuario_bp)
    app.register_blueprint(ingredientes_bp)
    app.register_blueprint(recetas_bp)
    app.register_blueprint(views_bp)

    return app
