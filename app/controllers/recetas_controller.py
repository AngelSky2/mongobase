from flask import request, jsonify
from bson import ObjectId
from app.models.receta import crear_receta_dict

# Crea una receta individual en la base de datos
def crear_receta(mongo, datos):
    # Si los ingredientes vienen como strings, conviértelos a ObjectId
    if "ingredientes_ids" in datos:
        datos["ingredientes_ids"] = [
            ObjectId(id) for id in datos.get("ingredientes_ids", []) if ObjectId.is_valid(id)
        ]
    receta = crear_receta_dict(datos)
    resultado = mongo.db.recetas.insert_one(receta)
    return str(resultado.inserted_id)

# Lista todas las recetas de la base de datos y las devuelve como JSON
def listar_recetas(mongo):
    recetas = mongo.db.recetas.find()
    lista = []
    for receta in recetas:
        receta['_id'] = str(receta['_id'])
        receta['ingredientes_ids'] = [str(id) for id in receta.get('ingredientes_ids', [])]
        for comentario in receta.get('comentarios', []):
            if 'usuario_id' in comentario:
                comentario['usuario_id'] = str(comentario['usuario_id'])
        lista.append(receta)
    return jsonify(lista)

# Crea múltiples recetas en la base de datos a partir de una lista de datos
def crear_recetas_multiples(mongo, lista_datos):
    recetas_formateadas = []
    for datos in lista_datos:
        if "ingredientes_ids" in datos:
            datos["ingredientes_ids"] = [
                ObjectId(id) for id in datos.get("ingredientes_ids", []) if ObjectId.is_valid(id)
            ]
        receta = crear_receta_dict(datos)
        recetas_formateadas.append(receta)
    resultado = mongo.db.recetas.insert_many(recetas_formateadas)
    return [str(id) for id in resultado.inserted_ids]
