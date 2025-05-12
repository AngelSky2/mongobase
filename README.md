# 🥗 API de Catálogo de Recetas

Una API construida con Flask y MongoDB para gestionar usuarios y recetas.

---

## 🚀 Requisitos

- Python 3.10+
- MongoDB (corriendo en `localhost:27017`)
- pip (administrador de paquetes de Python)
- Postman (opcional, para pruebas)

---

## 📦 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuración

Asegúrate de que MongoDB esté corriendo localmente (puerto 27017).  
Puedes cambiar la conexión en `app/__init__.py`:

```python
app.config["MONGO_URI"] = "mongodb://localhost:27017/catalogo_recetas"
```

---

## ▶️ Ejecutar la API

Desde la raíz del proyecto:

```bash
python run.py
```

Esto levantará el servidor en `http://localhost:5000`.

---

## 🧪 Pruebas con Postman

### Crear un usuario

- **Método:** `POST`
- **URL:** `http://localhost:5000/usuarios/crear`
- **Body (raw / JSON):**
```json
{
  "nombre": "Juan",
  "email": "juan@example.com"
}
```

### Listar usuarios

- **Método:** `GET`
- **URL:** `http://localhost:5000/usuarios/`

---

## 📂 Estructura de carpetas

```
.
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── models
│   │   └── usuario.py
│   ├── controllers
│   │   └── usuario_controller.py
│   └── routes
│       └── usuario_routes.py
├── run.py
├── requirements.txt
└── README.md
```

---

## 🛠 Tecnologías usadas

- Flask
- Flask-PyMongo
- MongoDB
- Flask-CORS