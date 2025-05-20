from flask import Blueprint, render_template, request, redirect, url_for
from bson import ObjectId
from bson.errors import InvalidId
from app import mongo

views_bp = Blueprint('views', __name__)

@views_bp.route('/')
def home():
    recetas = list(mongo.db.recetas.find())
    return render_template('index.html', recetas=recetas)

@views_bp.route('/receta')
def lista_recetas():
    recetas = list(mongo.db.recetas.find())
    return render_template('recetas.html', recetas=recetas)

@views_bp.route('/usuario')
def lista_usuarios():
    usuarios = list(mongo.db.usuarios.find())
    return render_template('usuario.html', usuarios=usuarios)

@views_bp.route('/receta/<id>', methods=['GET', 'POST'])
def ver_receta(id):
    try:
        receta = mongo.db.recetas.find_one({"_id": ObjectId(id)})
    except InvalidId:
        return "ID de receta inválido", 400

    if not receta:
        return "Receta no encontrada", 404

    ingredientes = []
    for ing_id in receta.get("ingredientes_ids", []):
        ing = mongo.db.ingredientes.find_one({"_id": ObjectId(ing_id)})
        if ing:
            ingredientes.append({"nombre": ing.get("nombre", "Desconocido")})

    # Agregar comentario
    if request.method == 'POST':
        nombre_usuario = request.form.get('nombre', '').strip()
        comentario_texto = request.form.get('comentario', '').strip()

        if not nombre_usuario or not comentario_texto:
            return "Nombre y comentario son obligatorios", 400

        nuevo_comentario = {
            "usuario": nombre_usuario,
            "comentario": comentario_texto
        }

        mongo.db.recetas.update_one(
            {"_id": ObjectId(id)},
            {"$push": {"comentarios": nuevo_comentario}}
        )

        return redirect(url_for('views.ver_receta', id=id))

    return render_template('detalle_receta.html', receta=receta, ingredientes=ingredientes)
