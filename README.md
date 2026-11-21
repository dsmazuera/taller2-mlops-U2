
# Proyecto 1 - Predicción de Enfermedades

## Descripción

Simulación de clasificación de enfermedades mediante una aplicación web.

## Variables de entrada

- Temperatura en grados Celsius.
- Intensidad de los síntomas de 0 a 10.
- Número de días con síntomas.

## Resultados posibles

- NO ENFERMO
- ENFERMEDAD LEVE
- ENFERMEDAD AGUDA
- ENFERMEDAD CRÓNICA


## Construcción de la imagen Docker

Desde la carpeta del proyecto ejecutar:

docker build -t mlops-enfermedades .

## Ejecución del contenedor

docker run --rm -p 5001:5001 mlops-enfermedades

## Acceso a la aplicación

Abrir en el navegador:

http://localhost:5001

