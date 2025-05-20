
def crear_ingrediente_dict(datos):
    return {
        "nombre": datos.get("nombre"),
        "tipo": datos.get("tipo"),
        "descripcion": datos.get("descripcion"),
        "costo_por_unidad": datos.get("costo_por_unidad"),
        "unidad": datos.get("unidad")
    }

