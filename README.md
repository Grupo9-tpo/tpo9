# Trivia Game

Este es un juego de trivia interactivo desarrollado en Python utilizando la biblioteca **tkinter** para la interfaz gráfica. El juego incluye preguntas categorizadas en distintas áreas de conocimiento y permite a los jugadores competir por puntos al responder correctamente.

## Características

- **Interfaz gráfica**: Utiliza `tkinter` para una experiencia de usuario amigable.
- **Categorías de preguntas**: Los jugadores pueden elegir entre diferentes categorías como **Entretenimiento**, **Deporte**, **Historia**, **Tecnología** y **Geografía**.
- **Puntajes guardados**: Los puntajes de los jugadores se almacenan en un archivo local para mantener un registro de las puntuaciones.
- **Dinámica del juego**: Cada categoría tiene 5 preguntas aleatorias, y cada respuesta correcta otorga 3 puntos.

## Requisitos

- Python 3.x instalado.
- Sistema operativo con soporte para Python (Windows, macOS, Linux).

## Archivos del proyecto

- `main.py`: Contiene la lógica principal del juego y la interfaz gráfica.
- `preguntas.py`: Archivo que almacena las preguntas y respuestas organizadas por categorías.
- `puntajes.txt`: Archivo que guarda los puntajes de los jugadores (se genera automáticamente al iniciar el juego si no existe).

## Instrucciones para jugar

1. Ejecutar el archivo `main.py`.
2. Ingresar tu nombre cuando se solicite.
3. Elegir una categoría para comenzar.
4. Responder las preguntas seleccionando la opción correcta.
5. Al completar todas las preguntas de una categoría, se pasará a otra categoría para continuar.
6. ¡Puedes salir del juego en cualquier momento, y tu puntuación se guardará automáticamente!

## Instalación y configuración

1. Clonar el repositorio o descargar los archivos del proyecto.
2. Asegúrate de que Python esté instalado y configurado en tu sistema.
3. Ejecutar el juego con el siguiente comando:

   ```bash
   python main.py
