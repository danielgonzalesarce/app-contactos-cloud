Markdown
# 📱 Aplicación Web de Agenda de Contactos

Este proyecto es una aplicación web dinámica desarrollada con **Flask (Python 3)** y **SQLite 3** para la gestión centralizada de una agenda de contactos (Nombres, Teléfonos y Correos electrónicos). 

Diseñado específicamente para el laboratorio de la unidad didáctica de **Desarrollo de Soluciones en la Nube** en Tecsup, bajo la supervisión del profesor **Jaime Farfán**. El proyecto está estructurado y optimizado para su posterior despliegue e instalación en instancias de infraestructura nube (**AWS EC2 con Windows Server y Debian Linux**).

---

## 📋 Requerimientos del Sistema
Antes de proceder con la instalación y ejecución del proyecto, asegúrate de contar con los siguientes componentes instalados en el sistema operativo:
* **Python 3.9 o superior** (Asegurarse de marcar la opción "Add Python to PATH" durante la instalación).
* **Git** (Para el control de versiones y clonación del repositorio).
* **Pip** (Administrador de paquetes de Python, incluido por defecto con Python).

---

## 📦 Estructura General del Proyecto
El repositorio mantiene estrictamente la siguiente jerarquía de directorios y archivos para garantizar el correcto funcionamiento del servidor web:
```text
app-contactos-cloud/
│
├── app.py               # Lógica del Backend (Flask), ruteo e inicialización de la Base de Datos
├── README.md            # Documentación técnica y guía de despliegue del proyecto
└── templates/
    └── index.html       # Interfaz gráfica de usuario / Frontend (HTML5 y CSS3 responsivo)
🚀 Guía de Instalación y Ejecución Local
Sigue paso a paso estas instrucciones en la consola o terminal de comandos de tu sistema para descargar, configurar y poner en marcha la aplicación desde cero:

1. Clonar el repositorio remoto
Abre tu terminal (Command Prompt, PowerShell o Git Bash) y descarga una copia exacta del proyecto con el siguiente comando:

Bash
git clone [https://github.com/danielgonzalesarce/app-contactos-cloud.git](https://github.com/danielgonzalesarce/app-contactos-cloud.git)
2. Acceder al directorio del proyecto
Desplázate hacia la carpeta que se acaba de crear tras la clonación:

Bash
cd app-contactos-cloud
3. Instalar las dependencias de Python
Ejecuta el gestor de paquetes de Python para descargar e instalar el framework web Flask:

Bash
pip install flask
4. Iniciar el servidor web local
Arranca el backend de la aplicación ejecutando el script principal de Python:

Bash
python app.py
5. Acceder a la aplicación web
Una vez que la terminal indique que el entorno de desarrollo está activo, abre tu navegador web e ingresa a cualquiera de las siguientes direcciones:

http://localhost:5000

http://127.0.0.1:5000

📊 Arquitectura de Datos y Persistencia
Motor de Base de Datos: Se utiliza SQLite 3, un sistema de gestión de bases de datos relacionales ligero, embebido y autónomo que no requiere configuraciones ni servicios adicionales de servidores externos.

Persistencia Automatizada: Al ejecutarse la aplicación por primera vez, el script app.py verifica y crea automáticamente un archivo de almacenamiento físico llamado contactos.db en la raíz del proyecto. Toda inserción o eliminación de registros persistirá de manera permanente dentro de este archivo.

Desarrollado como evidencia de laboratorio para Tecsup - 2026.


---

### 📤 Pasos finales en tu terminal para subirlo:
Una vez guardado el archivo con este texto dentro de tu computadora, ejecuta estos tres comandos rápidos en tu Git Bash o terminal para actualizar tu GitHub de inmediato:

```bash
git add README.md
git commit -m "Actualización de README con guía completa de instalación local"
git push origin main