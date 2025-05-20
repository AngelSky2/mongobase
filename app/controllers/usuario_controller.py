from flask import request, jsonify
from app import mongo
from app.models.usuario import crear_usuario_dict

# Crear un solo usuario
def crear():
    data = request.json
    usuario = crear_usuario_dict(data)
    mongo.db.usuarios.insert_one(usuario)
    return jsonify({"mensaje": "Usuario creado"}), 201

# Crear múltiples usuarios
def crear_multiples():
    lista_datos = request.json
    usuarios_creados = []

    for data in lista_datos:
        usuario = crear_usuario_dict(data)
        usuarios_creados.append(usuario)

    resultado = mongo.db.usuarios.insert_many(usuarios_creados)
    ids_creados = [str(id) for id in resultado.inserted_ids]

    return jsonify({"mensaje": "Usuarios creados", "ids": ids_creados}), 201

# Listar todos los usuarios
def listar():
    usuarios = list(mongo.db.usuarios.find())
    for u in usuarios:
        u["_id"] = str(u["_id"])
    return jsonify(usuarios)
