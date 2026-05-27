import sqlite3
from pathlib import Path

from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)
DB_PATH = Path(__file__).with_name("contactos.db")


def obtener_conexion():
    conexion = sqlite3.connect(DB_PATH)
    conexion.row_factory = sqlite3.Row
    return conexion


def inicializar_db():
    with obtener_conexion() as conexion:
        conexion.execute(
            """
            CREATE TABLE IF NOT EXISTS contactos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                telefono TEXT NOT NULL,
                email TEXT NOT NULL
            )
            """
        )
        conexion.commit()


@app.route("/", methods=["GET"])
def index():
    with obtener_conexion() as conexion:
        contactos = conexion.execute(
            "SELECT id, nombre, telefono, email FROM contactos ORDER BY id DESC"
        ).fetchall()

    return render_template("index.html", contactos=contactos)


@app.route("/agregar", methods=["POST"])
def agregar_contacto():
    nombre = request.form.get("nombre", "").strip()
    telefono = request.form.get("telefono", "").strip()
    email = request.form.get("email", "").strip()

    if nombre and telefono and email:
        with obtener_conexion() as conexion:
            conexion.execute(
                "INSERT INTO contactos (nombre, telefono, email) VALUES (?, ?, ?)",
                (nombre, telefono, email),
            )
            conexion.commit()

    return redirect(url_for("index"))


@app.route("/eliminar/<int:contacto_id>", methods=["POST"])
def eliminar_contacto(contacto_id):
    with obtener_conexion() as conexion:
        conexion.execute("DELETE FROM contactos WHERE id = ?", (contacto_id,))
        conexion.commit()

    return redirect(url_for("index"))


inicializar_db()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
