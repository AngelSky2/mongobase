# 🥗 Catálogo de Recetas Bolivia

Una aplicación web y API construida con Flask y MongoDB para gestionar usuarios y recetas bolivianas, con un diseño cyberpunk.

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

## ▶️ Ejecutar la aplicación

Desde la raíz del proyecto:

```bash
python run.py
```

Esto levantará el servidor en `http://localhost:5000`.

---

## 🖥️ ¿Cómo funciona la aplicación?

### 1. Inicio y navegación

- Al entrar a la web (`/`), ves un menú principal con enlaces a recetas y usuarios.
- El diseño es **cyberpunk**: fondo oscuro, colores neón, fuente futurista.

### 2. Recetas

- `/receta`: Lista todas las recetas en tarjetas (cards) con nombre, región, dificultad, tiempo y etiquetas.
- Cada receta tiene un botón para ver el detalle.

### 3. Detalle de receta

- `/receta/<id>`: Muestra toda la información de la receta seleccionada:
  - Ingredientes (con nombres obtenidos por ID)
  - Pasos de preparación
  - Comentarios de usuarios (y formulario para agregar uno nuevo)

### 4. Usuarios

- `/usuario`: Muestra una tabla con todos los usuarios registrados (nombre y email).

### 5. API REST

- **Usuarios:**  
  - Crear usuario: `POST /usuarios/crear`
  - Crear múltiples: `POST /usuarios/crear-multiples`
  - Listar: `GET /usuarios/`
- **Recetas:**  
  - Crear receta: `POST /recetas/crear`
  - Crear múltiples: `POST /recetas/crear-multiples`
  - Listar: `GET /recetas/`
- **Ingredientes:**  
  - Crear: `POST /ingredientes`
  - Listar: `GET /ingredientes`

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
mongobase/
│
├── app/
│   ├── __init__.py                # Inicializa la app y la conexión a MongoDB
│   ├── config.py
│   ├── controllers/               # Lógica de negocio para usuarios, recetas, ingredientes
│   ├── models/                    # Modelos de datos (estructura de usuario, receta, ingrediente)
│   ├── routes/                    # Rutas (API y vistas web)
│   └── templates/                 # Plantillas HTML (Jinja2)
│
├── run.py                         # Script principal para arrancar la app
├── requirements.txt               # Dependencias del proyecto
├── recetas.json                   # Datos de ejemplo de recetas
├── ingredientes.json              # Datos de ejemplo de ingredientes
├── usuarios.json                  # Datos de ejemplo de usuarios
└── README.md                      # Documentación del proyecto
```

---

## 🛠 Tecnologías usadas

- Flask
- Flask-PyMongo
- MongoDB
- Flask-CORS
- Bootstrap 5
- Jinja2

---

## 🧩 Modelos de datos

- **Usuario:**  
  - `nombre`: Nombre del usuario  
  - `email`: Email del usuario  
  - `recetas_creadas`: Lista de recetas creadas  
  - `recetas_favoritas`: Lista de recetas favoritas

- **Receta:**  
  - `nombre`, `tipo`, `dificultad`, `region_origen`, `foto`, `notas`, `tiempo_preparacion`, `porciones`, `etiquetas`, `ingredientes_ids`, `pasos`, `comentarios`

- **Ingrediente:**  
  - `nombre`, `tipo`, `descripcion`, `costo`, `unidad`

---

## 🎨 Personalización visual

- El diseño es **cyberpunk**:  
  - Cards con fondo degradado y bordes neón.
  - Títulos de recetas en verde fosforescente.
  - Botones y textos con efectos brillantes.
  - Fuente Orbitron de Google Fonts.

---

## 🗄️ ¿Cómo funciona MongoDB en este proyecto?

- **MongoDB** es una base de datos NoSQL orientada a documentos.
- Cada colección (por ejemplo, `usuarios`, `recetas`, `ingredientes`) almacena documentos en formato JSON/BSON.
- Flask se conecta a MongoDB usando **Flask-PyMongo**.
- Las operaciones CRUD (crear, leer, actualizar, borrar) se hacen directamente sobre las colecciones.
- Ejemplo de inserción de usuario:
  ```python
  mongo.db.usuarios.insert_one({
      "nombre": "Juan",
      "email": "juan@example.com",
      "recetas_creadas": [],
      "recetas_favoritas": []
  })
  ```
- Para obtener datos, se usan métodos como `find()` y `find_one()`:
  ```python
  usuarios = list(mongo.db.usuarios.find())
  ```
- Los IDs de los documentos son generados automáticamente por MongoDB (`_id`).

---

## 📢 Créditos

Desarrollado por [Tu Nombre o Equipo].

---