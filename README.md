# Sistema de recomendación de películas

Proyecto desarrollado como actividad formativa de inteligencia artificial y GitHub Copilot. Permite explorar películas recomendadas por género y por un rango de años.

## Objetivos

- Construir una página web en español para explorar recomendaciones.
- Filtrar películas por género y por año de inicio y término.
- Implementar en Python un recomendador que prioriza las películas mejor calificadas dentro de los filtros elegidos.
- Documentar el proceso de desarrollo y preparar el proyecto para su publicación en GitHub.

## Proceso de implementación

### 1. Preparación del repositorio

Se trabajó en el repositorio `AI_Project`, cuyo remoto `origin` apunta a [rodrigocutinoa/AI_Project](https://github.com/rodrigocutinoa/AI_Project). El proyecto contiene un `.gitignore` para excluir, entre otros archivos, entornos virtuales y archivos de caché de Python.

La guía de la actividad propone crear o solicitar acceso a GitHub Copilot, crear el repositorio y clonarlo en Visual Studio Code. Esta documentación describe el estado del proyecto de código; no constituye evidencia del estado de una cuenta académica o de una licencia de estudiante.

### 2. Definición del catálogo de películas

Se preparó un catálogo de 12 películas de ejemplo. Cada registro contiene título, año de estreno, calificación y uno o más géneros. El catálogo incluye géneros como Acción, Animación, Aventura, Ciencia ficción, Comedia, Drama, Fantasía, Romance y Suspenso.

Los mismos títulos, años, géneros y calificaciones se utilizaron en la interfaz y en el programa Python. Los datos son ejemplos incorporados al proyecto: no provienen de una API ni de una base de datos externa.

### 3. Construcción de la interfaz web

En [`index.html`](./index.html) se implementó una página autónoma con HTML, CSS y JavaScript:

1. Se creó una cabecera y una sección introductoria para presentar el propósito de la página.
2. Se agregaron los controles para seleccionar un género e indicar los años «Desde» y «Hasta».
3. Se implementaron tarjetas con título, año, calificación y etiquetas de género.
4. Se añadió el contador de resultados, el botón para limpiar los filtros y un mensaje para búsquedas sin coincidencias.
5. Se adaptó la distribución para pantallas de escritorio y dispositivos móviles.

Los filtros se aplican en conjunto: una película debe coincidir con el género seleccionado, si lo hay, y estar dentro de ambos límites de año, si se especificaron.

### 4. Implementación del recomendador en Python

En [`recommendation_system.py`](./recommendation_system.py) se definió un modelo `Movie` y el catálogo de películas. La función `recommend_movies` filtra por género y rango inclusivo de años, y ordena las coincidencias por calificación descendente. Si dos películas tienen la misma calificación, el título se utiliza como criterio secundario de orden.

El programa de terminal acepta estas opciones:

- `--genero`: género seleccionado; si se omite, no se filtra por género.
- `--desde`: año inicial inclusivo; si se omite, no se aplica límite inferior.
- `--hasta`: año final inclusivo; si se omite, no se aplica límite superior.
- `--limite`: cantidad máxima de resultados; por defecto es `5`.

Se incorporaron validaciones para géneros no disponibles, años que no sean enteros, rangos invertidos y límites menores que uno. Si no hay coincidencias, se muestra un mensaje informativo.

### 5. Pruebas realizadas

Se verificó la sintaxis de Python y se ejecutaron comprobaciones funcionales para:

- Confirmar que el catálogo contiene 12 películas.
- Filtrar por Acción y por los años 2015–2020, incluidos ambos extremos.
- Confirmar que los resultados se ordenan por calificación.
- Comprobar que un rango sin películas devuelve una lista vacía.
- Comprobar que los filtros y el límite rechazan entradas inválidas.
- Probar la ejecución del recomendador desde la terminal.

La interfaz web también se probó en el navegador con filtros combinados, un caso sin resultados y el botón «Limpiar filtros».

## Ejecución

No se requieren paquetes externos para ejecutar el recomendador Python. Desde la carpeta del proyecto:

```bash
python3 recommendation_system.py
```

Ejemplo con filtros:

```bash
python3 recommendation_system.py --genero "Acción" --desde 2015 --hasta 2020
```

La salida para ese ejemplo es:

```text
Recomendaciones:
- Spider-Man: Un nuevo universo (2018) | ★ 8.4 | Animación, Acción, Aventura
- Mad Max: Furia en el camino (2015) | ★ 8.1 | Acción, Aventura, Ciencia ficción
```

Para abrir la interfaz, abre [`index.html`](./index.html) en un navegador. También se puede iniciar un servidor local estático desde la carpeta del proyecto:

```bash
python3 -m http.server 8000
```

Luego visita <http://localhost:8000>.

## Alcance actual

La interfaz HTML y el recomendador Python funcionan como dos formas independientes de consultar el catálogo. La página web filtra sus datos localmente en JavaScript; no invoca el módulo Python. El programa Python entrega recomendaciones por terminal. El proyecto no incluye todavía un servidor web, una API, persistencia de datos ni integración con servicios externos.

## Evidencias visuales para la entrega

La guía docente solicita incorporar capturas de pantalla con una descripción de cada paso. Las capturas no estaban incluidas entre los archivos disponibles al redactar este documento; por ello, esta sección identifica las evidencias que se deben capturar y agregar antes de entregar:

| Evidencia sugerida | Descripción |
| --- | --- |
| `docs/capturas/01-repositorio.png` | Repositorio `AI_Project` en GitHub y archivos del proyecto. |
| `docs/capturas/02-codigo-python.png` | `recommendation_system.py` abierto en Visual Studio Code, mostrando la función de recomendación y sus argumentos. |
| `docs/capturas/03-pagina-web.png` | `index.html` abierto en el navegador con las recomendaciones y los filtros visibles. |
| `docs/capturas/04-filtros-aplicados.png` | Resultado de la página o de la terminal después de aplicar un género y un rango de años. |

Al tomar las capturas, guárdalas en `docs/capturas/` y reemplaza esta lista por imágenes Markdown y sus descripciones. Evita incluir credenciales, datos personales u otra información sensible.

## Publicación de cambios en GitHub

Una vez revisados los archivos y añadidas las evidencias requeridas, los cambios se pueden publicar desde la terminal integrada de Visual Studio Code:

```bash
git add README.md index.html recommendation_system.py
git add docs/capturas/
git commit -m "Documenta el proceso del sistema de recomendaciones"
git push -u origin HEAD
```

El segundo comando se utiliza después de agregar las capturas. Si todavía no se han creado, omítelo. Después de publicar los cambios, comparte la URL del repositorio siguiendo las instrucciones de entrega del docente.
