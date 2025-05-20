def crear_receta_dict(datos):
    return {
        "nombre": datos.get("nombre"),
        "tipo_comida": datos.get("tipo_comida"),
        "dificultad": datos.get("dificultad"),
        "region_origen": datos.get("region_origen"),
        "foto": datos.get("foto"),
        "notas": datos.get("notas"),
        "tiempo_preparacion": datos.get("tiempo_preparacion"),
        "porciones": datos.get("porciones"),
        "etiquetas": datos.get("etiquetas"),
        "ingredientes_ids": datos.get("ingredientes_ids"),  
        "pasos": datos.get("pasos"),
        "comentarios": datos.get("comentarios", [])
    }

