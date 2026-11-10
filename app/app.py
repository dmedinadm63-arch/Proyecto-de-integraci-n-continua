from flask import Flask, jsonify
import mysql.connector
import os
import time

app = Flask(__name__)

def conectar():
    for intento in range(10):
        try:
            conexion = mysql.connector.connect(
                host=os.getenv("DB_HOST", "db"),
                user=os.getenv("DB_USER", "estudiante"),
                password=os.getenv("DB_PASSWORD", "estudiante123"),
                database=os.getenv("DB_NAME", "universidad")
            )
            return conexion
        except mysql.connector.Error:
            time.sleep(3)
    return None

@app.route("/")
def inicio():
    return """
    <h1>Proyecto de Integración Continua</h1>
    <p>Aplicación web funcionando correctamente.</p>
    <p>Contenedor web conectado con una base de datos.</p>
    <a href='/estudiantes'>Consultar estudiantes</a>
    """

@app.route("/estudiantes")
def estudiantes():
    conexion = conectar()

    if conexion is None:
        return jsonify({"error": "No fue posible conectar con la base de datos"}), 500

    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT id, nombre FROM estudiantes")
    datos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return jsonify(datos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
