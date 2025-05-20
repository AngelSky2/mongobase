def crear_usuario_dict(datos):
    return {
        "nombre": datos.get("nombre"),
        "email": datos.get("email"),
        "recetas_creadas": [],
        "recetas_favoritas": []
    }

