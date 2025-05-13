from flask import request, jsonify
from bson import ObjectId
#funcion para crear recetas 

def crear_receta(mongo, datos):
    receta = {
        "nombre": datos.get("nombre", "Sin nombre"),
        "tipo_comida": datos.get("tipo_comida", "Desconocido"),
        "dificultad": datos.get("dificultad", "Media"),
        "region_origen": datos.get("region_origen", "Desconocida"),
        "foto": datos.get("foto", ""),  # URL opcional
        "notas": datos.get("notas", ""),
        "tiempo_preparacion": datos.get("tiempo_preparacion", 0),
        "porciones": datos.get("porciones", 1),
        "etiquetas": datos.get("etiquetas", []),
        "ingredientes_ids": [
            ObjectId(id) for id in datos.get("ingredientes_ids", []) if ObjectId.is_valid(id)
        ],
        "pasos": datos.get("pasos", []),
        "comentarios": datos.get("comentarios", [])
    }

    resultado = mongo.db.recetas.insert_one(receta)
    return str(resultado.inserted_id)
#funcion de listar las recetas
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

def crear_recetas_multiples(mongo, lista_datos):
    recetas_formateadas = []

    for datos in lista_datos:
        receta = {
            "nombre": datos.get("nombre"),
            "tipo_comida": datos.get("tipo_comida"),
            "dificultad": datos.get("dificultad"),
            "region_origen": datos.get("region_origen"),
            "foto": datos.get("foto"),
            "notas": datos.get("notas"),
            "tiempo_preparacion": datos.get("tiempo_preparacion"),
            "porciones": datos.get("porciones"),
            "etiquetas": datos.get("etiquetas"),
            "ingredientes_ids": [
                ObjectId(id) for id in datos.get("ingredientes_ids", []) if ObjectId.is_valid(id)
            ],
            "pasos": datos.get("pasos"),
            "comentarios": datos.get("comentarios", [])
        }
        recetas_formateadas.append(receta)

    resultado = mongo.db.recetas.insert_many(recetas_formateadas)
    return [str(id) for id in resultado.inserted_ids]
