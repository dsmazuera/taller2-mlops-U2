
from flask import Flask, request

app = Flask(__name__)

def predecir_enfermedad(temperatura, intensidad, dias):
    if temperatura >= 40 and intensidad >= 9 and dias >= 15:
        return "ENFERMEDAD TERMINAL"
    if dias >= 30:
        return "ENFERMEDAD CRÓNICA"
    elif temperatura >= 39 or intensidad >= 8:
        return "ENFERMEDAD AGUDA"
    elif temperatura >= 37.5 or intensidad >= 3:
        return "ENFERMEDAD LEVE"
    else:
        return "NO ENFERMO"


@app.route("/", methods=["GET", "POST"])
def inicio():
    resultado = ""

    if request.method == "POST":
        try:
            temperatura = float(request.form["temperatura"])
            intensidad = int(request.form["intensidad"])
            dias = int(request.form["dias"])

            if 30 <= temperatura <= 45 and 0 <= intensidad <= 10 and dias >= 0:
                resultado = predecir_enfermedad(
                    temperatura, intensidad, dias
                )
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
            <input type="number" name="temperatura" step="0.1" required>

            <p>Intensidad de síntomas (0-10):</p>
            <input type="number" name="intensidad" min="0" max="10" required>

            <p>Días con síntomas:</p>
            <input type="number" name="dias" min="0" required>

            <p><button type="submit">Predecir</button></p>
        </form>

        <h3>Resultado: RESULTADO_AQUI</h3>
        <p>Simulación académica. No es un diagnóstico médico.</p>
    </body>
    </html>
    """.replace("RESULTADO_AQUI", resultado)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

