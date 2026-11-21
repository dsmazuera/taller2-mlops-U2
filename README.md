
# Taller 2 - MLOps: Predicción de Enfermedades
Leandro Avila - Diana Mazuera

## 1. Descripción del proyecto

Aplicación web que simula la clasificación de enfermedades a partir de tres variables ingresadas por el usuario. 

El proyecto permite registrar las predicciones, consultar estadísticas y visualizar los resultados mediante una interfaz web.

Como parte del Taller 2, se incorporaron pruebas automatizadas, integración continua y publicación automática de una imagen Docker mediante GitHub Actions.

## 2. Tecnologías utilizadas

- Python
- Flask
- HTML y CSS
- Docker
- Git y GitHub
- GitHub Actions
- GitHub Container Registry (GHCR)

## 3. Variables de entrada

La aplicación recibe tres variables:

| Variable | Descripción | Valores |
|---|---|---|
| Temperatura | Temperatura corporal en grados Celsius | 30 a 45 |
| Intensidad | Intensidad de los síntomas | 0 a 10 |
| Días | Número de días con síntomas | 0 o más |

## 4. Categorías de predicción

El simulador clasifica los datos ingresados en una de las siguientes cinco categorías:

1. NO ENFERMO
2. ENFERMEDAD LEVE
3. ENFERMEDAD AGUDA
4. ENFERMEDAD CRÓNICA
5. ENFERMEDAD TERMINAL

La clasificación se realiza mediante reglas condicionales definidas en el archivo `app.py`.

No se utiliza un modelo clínico entrenado con datos reales.

## 5. Funcionalidades principales

### Simulador de predicción

Ingresar la temperatura corporal, la intensidad de los síntomas y el número de días con síntomas del paciente. La aplicación procesa estos valores y muestra la categoría correspondiente.

### Registro de predicciones

Cada predicción se guarda con:

- Fecha y hora de ejecución.
- Categoría obtenida.

Los registros se almacenan en el archivo:

`data/predicciones.jsonl`

### Panel de estadísticas

El sistema permite consultar:

- Número total de predicciones.
- Cantidad de predicciones por categoría.
- Últimas cinco predicciones realizadas.
- Fecha y hora de la predicción más reciente.

Las estadísticas se presentan mediante un panel visual desarrollado con HTML y CSS.

## 6. Rutas de la aplicación

| Ruta | Descripción |
|---|---|
| `/` | Formulario principal de predicción |
| `/estadisticas` | Panel visual de estadísticas |
| `/api/estadisticas` | Estadísticas en formato JSON |

## 7. Ejecución local con Python

### Instalar dependencias

Desde la carpeta principal del proyecto:

```bash
python -m pip install -r requirements.txt
```

### Iniciar la aplicación

```bash
python app.py
```

### Abrir el navegador

Acceder a:

http://localhost:5001

## 8. Ejecución con Docker

### Construir la imagen

Desde la carpeta principal del proyecto:

```bash
docker build -t mlops-enfermedades .
```

### Ejecutar el contenedor

```bash
docker run --rm -p 5001:5001 mlops-enfermedades
```

### Acceder a la aplicación

Abrir:

http://localhost:5001

Para detener el contenedor, presionar `Ctrl + C`.

**Nota:** Los registros generados dentro del contenedor no se conservan después de eliminarlo, a menos que se configure almacenamiento persistente.

## 9. Pruebas automatizadas

El proyecto contiene pruebas automatizadas para verificar el funcionamiento de la aplicación.

Las pruebas se encuentran en:

`tests/test_app.py`

Para ejecutarlas localmente:

```bash
python -m pytest -v
```

Estas pruebas también se ejecutan automáticamente mediante GitHub Actions.

## 10. Integración continua y despliegue continuo

El proyecto utiliza GitHub Actions para automatizar las pruebas y la publicación de la imagen Docker.

El flujo se encuentra definido en:

`.github/workflows/ci-cd.yml`

### Al crear un Pull Request hacia main

GitHub Actions:

1. Publica un comentario indicando el inicio
   del proceso de CI/CD.
2. Ejecuta las pruebas automatizadas.
3. Publica un comentario cuando el proceso termina correctamente.

### Al incorporar cambios a main

GitHub Actions:

1. Ejecuta las pruebas automatizadas.
2. Construye la imagen Docker.
3. Publica la imagen en GitHub Container Registry (GHCR).

Esto permite comprobar los cambios antes de incorporarlos a la rama principal y automatizar la construcción de la imagen.

## 11. Control de versiones

El desarrollo se realizó utilizando Git y GitHub. Se emplearon ramas de trabajo y Pull Requests para incorporar las funcionalidades del proyecto.

Entre las mejoras realizadas se encuentran:

- Incorporación de los archivos iniciales.
- Adición de la quinta categoría de enfermedad.
- Implementación del registro de predicciones.
- Desarrollo de estadísticas e historial.
- Incorporación de pruebas automatizadas.
- Configuración de GitHub Actions.
- Publicación automática de Docker.
- Mejoras visuales del simulador y del dashboard des historial-estadísticas.

La rama principal del proyecto es `main`.

## 12. Estructura del proyecto

```text
taller2-mlops-U2/
|
|-- app.py
|-- Dockerfile
|-- requirements.txt
|-- README.md
|-- .gitignore
|
|-- .github/
|   |-- workflows/
|       |-- ci-cd.yml
|
|-- templates/
|   |-- pagina_prediccion.html
|   |-- estadisticas.html
|
|-- tests/
|   |-- test_app.py
|
|-- data/
    |-- predicciones.jsonl
```

La carpeta `data` se crea automáticamente cuando se guarda una predicción.

## 13. Repositorio

Código fuente del proyecto:

https://github.com/dsmazuera/taller2-mlops-U2










