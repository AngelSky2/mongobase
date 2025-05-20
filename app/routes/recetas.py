from flask import Blueprint, request, jsonify
from app.controllers.recetas_controller import crear_receta, crear_recetas_multiples, listar_recetas
from app import mongo

recetas_bp = Blueprint('recetas', __name__, url_prefix='/recetas')

@recetas_bp.route('/crear', methods=['POST'])
def crear():
    datos = request.get_json()
    if not datos:
        return jsonify({"error": "No se proporcionaron datos"}), 400
    try:
        id_nueva_receta = crear_receta(mongo, datos)
        return jsonify({"mensaje": "Receta creada", "id": id_nueva_receta}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@recetas_bp.route('/', methods=['GET'])
def listar():
    return listar_recetas(mongo)

@recetas_bp.route('/crear-multiples', methods=['POST'])
def crear_multiples_recetas():
    try:
        data = request.get_json(force=True)
        if not isinstance(data, list):
            return jsonify({"error": "Se esperaba una lista de recetas"}), 400
        for receta in data:
            if not isinstance(receta, dict):
                return jsonify({"error": "Cada receta debe ser un diccionario"}), 400
        ids_creados = crear_recetas_multiples(mongo, data)
        return jsonify({"mensaje": "Recetas creadas", "ids": ids_creados}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500