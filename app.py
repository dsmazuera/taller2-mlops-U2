
import json
import os
from collections import Counter
from datetime import datetime, timezone
from flask import Flask, request, jsonify

app = Flask(__name__)

ARCHIVO = os.environ.get(
    "PREDICCIONES_FILE", "/app/data/predicciones.jsonl"
)

CATEGORIAS = [
    "NO ENFERMO",
    "ENFERMEDAD LEVE",
    "ENFERMEDAD AGUDA",
    "ENFERMEDAD CRÓNICA",
    "ENFERMEDAD TERMINAL"
]


# Función original con la quinta categoría
def predecir_enfermedad(temperatura, intensidad, dias):
    if temperatura >= 40 and intensidad >= 9 and dias >= 15:
        return "ENFERMEDAD TERMINAL"
    elif dias >= 30:
        return "ENFERMEDAD CRÓNICA"
    elif temperatura >= 39 or intensidad >= 8:
        return "ENFERMEDAD AGUDA"
    elif temperatura >= 37.5 or intensidad >= 3:
        return "ENFERMEDAD LEVE"
    else:
        return "NO ENFERMO"


# Guardar cada predicción
def guardar_prediccion(categoria):
    fecha = datetime.now(timezone.utc).isoformat()

    registro = {
        "fecha": fecha,
        "categoria": categoria
    }

    carpeta = os.path.dirname(ARCHIVO)
    if carpeta:
        os.makedirs(carpeta, exist_ok=True)

    with open(ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(
            json.dumps(registro, ensure_ascii=False) + "\n"
        )


# Leer las predicciones guardadas
def leer_predicciones():
    if not os.path.exists(ARCHIVO):
        return []

    registros = []

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if linea.strip():
                registros.append(json.loads(linea))

    return registros


# Calcular estadísticas
def calcular_estadisticas():
    registros = leer_predicciones()

    conteo = Counter(
        registro["categoria"] for registro in registros
    )

    por_categoria = {
        categoria: conteo.get(categoria, 0)
        for categoria in CATEGORIAS
    }

    return {
        "total_predicciones": len(registros),
        "predicciones_por_categoria": por_categoria,
        "ultimas_5_predicciones": list(
            reversed(registros[-5:])
        ),
        "fecha_ultima_prediccion": (
            registros[-1]["fecha"] if registros else None
        )
    }


# Página principal
@app.route("/", methods=["GET", "POST"])
def inicio():
    resultado = ""

    if request.method == "POST":
        try:
            temperatura = float(request.form["temperatura"])
            intensidad = int(request.form["intensidad"])
            dias = int(request.form["dias"])

            if (
                30 <= temperatura <= 45
                and 0 <= intensidad <= 10
                and dias >= 0
            ):
                resultado = predecir_enfermedad(
                    temperatura, intensidad, dias
                )
                guardar_prediccion(resultado)
            else:
                resultado = "Error: revisa los valores ingresados."

        except (ValueError, KeyError):
            resultado = "Error: introduce valores válidos."

    return """
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Predicción de Enfermedades</title>
    </head>
    <body>
        <h2>Simulador de Predicción de Enfermedades</h2>

        <form method="POST">
            <p>Temperatura (°C):</p>
            <input type="number" name="temperatura"
                   step="0.1" required>

            <p>Intensidad de síntomas (0-10):</p>
            <input type="number" name="intensidad"
                   min="0" max="10" required>

            <p>Días con síntomas:</p>
            <input type="number" name="dias"
                   min="0" required>

            <p><button type="submit">Predecir</button></p>
        </form>

        <h3>Resultado: RESULTADO_AQUI</h3>

        <p><a href="/estadisticas">
            Consultar estadísticas
        </a></p>

        <p>Simulación académica.
        No es un diagnóstico médico.</p>
    </body>
    </html>
    """.replace("RESULTADO_AQUI", resultado)


# Nueva ruta para consultar estadísticas
@app.route("/estadisticas", methods=["GET"])
def estadisticas():
    return jsonify(calcular_estadisticas())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)


