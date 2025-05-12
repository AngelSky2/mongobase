from flask import request, jsonify
from app import mongo
from app.models.usuario import crear_usuario

def crear():
    data = request.json
    usuario = crear_usuario(data['nombre'],data['email'])
    mongo.db.usuarios.insert_one(usuario)
    return jsonify({"mensaje":"usuario creado"}),201

def listar():
    usuarios = list(mongo.db.usuarios.find())
    for u in usuarios:
        u["_id"]=str(u["_id"])
    return jsonify(usuarios)