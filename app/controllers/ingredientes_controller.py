from flask import request, jsonify
from bson import ObjectId
from app.models.ingrediente import crear_ingrediente_dict

# Función para crear uno o varios ingredientes
def crear_ingredientes(mongo):
    datos = request.get_json()

    if isinstance(datos, dict):
        ingrediente = crear_ingrediente_dict(datos)
        resultado = mongo.db.ingredientes.insert_one(ingrediente)
        return jsonify({"mensaje": "Ingrediente creado", "id": str(resultado.inserted_id)}), 201

    elif isinstance(datos, list):
        ingredientes = [crear_ingrediente_dict(item) for item in datos]
        resultado = mongo.db.ingredientes.insert_many(ingredientes)
        return jsonify({
            "mensaje": "Ingredientes creados",
            "ids": [str(id) for id in resultado.inserted_ids]
        }), 201

    else:
        return jsonify({"error": "Formato no válido. Envía un objeto o una lista de objetos JSON."}), 400

# Función para listar los ingredientes
def listar_ingredientes(mongo):
    ingredientes = mongo.db.ingredientes.find()
    lista = []
    for ing in ingredientes:
        ing['_id'] = str(ing['_id'])
        lista.append(ing)
    return jsonify(lista)
