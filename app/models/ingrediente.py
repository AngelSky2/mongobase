from bson import ObjectId

def crear_ingrediente(mongo, datos):
    ingrediente = {
        "nombre": datos.get("nombre"),
        "tipo": datos.get("tipo"),
        "descripcion": datos.get("descripcion"),
        "costo_por_unidad": datos.get("costo_por_unidad"),
        "unidad": datos.get("unidad")
    }
    resultado = mongo.db.ingredientes.insert_one(ingrediente)
    return str(resultado.inserted_id)