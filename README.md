# 📱 Aplicación Web de Agenda de Contactos

Aplicación web desarrollada con **Flask (Python 3)** y **SQLite3** para la gestión de contactos.  
Permite registrar, visualizar y eliminar contactos almacenados localmente en una base de datos ligera.

Proyecto realizado para el laboratorio de la unidad didáctica de **Desarrollo de Soluciones en la Nube** en **Tecsup**, bajo la supervisión del profesor **Jaime Farfán**.

---

# 🚀 Tecnologías Utilizadas

- Python 3
- Flask
- SQLite3
- HTML5
- CSS3

---

# 📂 Estructura del Proyecto

```text
app-contactos-cloud/
│
├── app.py
├── contactos.db
├── README.md
└── templates/
    └── index.html
```

---

# ⚙️ Requisitos Previos

Antes de ejecutar el proyecto debes tener instalado:

- Python 3.9 o superior
- Pip
- Git

Verifica las instalaciones:

```bash
python --version
pip --version
git --version
```

---

# 📥 Instalación del Proyecto

## 1. Clonar el repositorio

```bash
git clone https://github.com/danielgonzalesarce/app-contactos-cloud.git
```

---

## 2. Ingresar al directorio

```bash
cd app-contactos-cloud
```

---

## 3. Instalar Flask

```bash
pip install flask
```

---

# ▶️ Ejecutar la Aplicación

Ejecuta el servidor Flask:

```bash
python app.py
```

---

# 🌐 Acceder desde el Navegador

Abrir cualquiera de las siguientes URLs:

```text
http://localhost:5000
```

o

```text
http://127.0.0.1:5000
```

---

# 🗄️ Base de Datos

La aplicación utiliza **SQLite3**.

Al iniciar por primera vez:

- Se crea automáticamente el archivo:

```text
contactos.db
```

- También se crea automáticamente la tabla:

```sql
contactos
```

---

# 📊 Consultar Datos desde Python

Abrir el intérprete de Python:

```bash
python
```

Ejecutar:

```python
import sqlite3

conn = sqlite3.connect("contactos.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM contactos")

for fila in cursor.fetchall():
    print(f"ID: {fila[0]} | Nombre: {fila[1]} | Teléfono: {fila[2]} | Email: {fila[3]}")
```

Salir del intérprete:

```python
exit()
```

---

# ✨ Funcionalidades

- Registrar contactos
- Listar contactos
- Eliminar contactos
- Persistencia de datos con SQLite
- Interfaz web responsiva
- Backend con Flask

---

# ☁️ Preparado para Despliegue Cloud

El proyecto está estructurado para facilitar su despliegue en:

- AWS EC2
- Windows Server
- Debian Linux

---

# 👨‍💻 Autor

Desarrollado como evidencia académica para **Tecsup — 2026**.