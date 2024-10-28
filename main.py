import random
import os  #Manejo de archivos y rutas
from preguntas import preguntas #Import de preguntas.py

#Nombre del archivo donde se guardarán los puntajes
registro_puntajes = "puntajes.txt"

#Verificar si el archivo de puntajes existe; si no, crearlo vacío
def inicializar_archivo():
    if not os.path.exists(registro_puntajes):
        with open(registro_puntajes, "w") as archivo:
            archivo.write("")

#Función de bienvenida
def bienvenida():
    print("¡Bienvenido a Triviathon!")

#Guardar puntaje con manejo de errores
def guardar_puntaje(nombre, puntuacion):
    try:
        with open(registro_puntajes, "a") as archivo:
            archivo.write(f"{nombre},{puntuacion}\n")
    except Exception as e:
        print(f"Error al guardar el puntaje: {e}")

#Seleccionar una categoría aleatoria que no se haya jugado
def seleccionar_categoria(categorias_jugadas):
    categorias_disponibles = [cat for cat in preguntas.keys() if cat not in categorias_jugadas]
    return random.choice(categorias_disponibles)

#Jugar la trivia
def jugar_trivia(categorias_jugadas):
    categoria = seleccionar_categoria(categorias_jugadas)
    print(f"Se ha seleccionado la categoría: {categoria}")

    preguntas_categoria = preguntas[categoria]
    random.shuffle(preguntas_categoria)

    puntuacion = 0
    num_preguntas = min(5, len(preguntas_categoria))

    for i in range(num_preguntas):
        pregunta_actual = preguntas_categoria[i]
        print(f"Pregunta {i + 1}: {pregunta_actual['pregunta']}")

        for j, opcion in enumerate(pregunta_actual['opciones']):
            print(f"{j + 1}. {opcion}")

        respuesta = input("Selecciona la opción correcta: ")
        if respuesta.isdigit() and 1 <= int(respuesta) <= len(pregunta_actual['opciones']):
            seleccion = pregunta_actual['opciones'][int(respuesta) - 1]
            if seleccion.lower() == pregunta_actual['respuesta'].lower():
                puntuacion += 3
                print("¡Correcto! +3 puntos")
            else:
                print(f"Incorrecto. La respuesta correcta era: {pregunta_actual['respuesta']}")
        else:
            print("Opción inválida. Por favor, elige un número.")

        print(f"Puntuación actual: {puntuacion}\n")

    return categoria, puntuacion

#Función principal del juego
def main():
    inicializar_archivo()
    bienvenida()

    categorias_jugadas = []
    historial_puntos = []
    nombre = input("Ingresa tu nombre: ")

    while len(categorias_jugadas) < 3:
        categoria, puntos = jugar_trivia(categorias_jugadas)
        categorias_jugadas.append(categoria)
        historial_puntos.append((categoria, puntos))

        if len(categorias_jugadas) == 3:
            print("\n¡Has jugado las 3 categorías! Fin del juego.")
            break

        continuar = input("¿Deseas seguir jugando? (s/n): ").lower()
        if continuar != 's':
            print("\nHas decidido finalizar el juego.")
            break

    puntaje_total = sum(puntos for _, puntos in historial_puntos)
    guardar_puntaje(nombre, puntaje_total)

    print("\nHistorial de puntos:")
    for categoria, puntos in historial_puntos:
        print(f"Categoría: {categoria}, Puntos: {puntos}")

    print(f"\nPuntuación total: {puntaje_total}")

#Ejecutar el programa
main()

