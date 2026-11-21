

import json
import os
from collections import Counter
from datetime import datetime, timezone
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Archivo donde se guardan las predicciones
ARCHIVO = os.environ.get(
    "PREDICCIONES_FILE",
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "data",
        "predicciones.jsonl"
    )
)

# Categorías de enfermedades
CATEGORIAS = [
    "NO ENFERMO",
    "ENFERMEDAD LEVE",
    "ENFERMEDAD AGUDA",
    "ENFERMEDAD CRÓNICA",
    "ENFERMEDAD TERMINAL"
]


# Función de predicción
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


# Página principal: simulador de enfermedades
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
                    temperatura,
                    intensidad,
                    dias
                )

                guardar_prediccion(resultado)

            else:
                resultado = "Error: revisa los valores ingresados."

        except (ValueError, KeyError):
            resultado = "Error: introduce valores válidos."

    # Mostrar la página con el diseño moderno
    return render_template(
        "pagina_prediccion.html",
        resultado=resultado
    )


# Página visual de estadísticas
@app.route("/estadisticas", methods=["GET"])
def estadisticas():

    datos = calcular_estadisticas()

    return render_template(
        "estadisticas.html",
        datos=datos
    )


# API para consultar estadísticas en JSON
@app.route("/api/estadisticas", methods=["GET"])
def api_estadisticas():

    return jsonify(calcular_estadisticas())


# Ejecutar aplicación
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5001
    )
