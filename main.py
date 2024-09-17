# Importar los diccionarios desde preguntas.py
from preguntas import preguntas

#Funciones

# Función de bienvenida
def bienvenida():
    print("¡Bienvenido a Triviathon!")

# Función para seleccionar categoría
def seleccionar_categoria():
    print("Selecciona una categoría:")
    print("1. Entretenimiento")
    print("2. Deporte")
    print("3. Geografía")

    categoria = input("Ingrese el número de la categoría que desea jugar: ")
    if categoria == "1":
        return "Entretenimiento"
    elif categoria == "2":
        return "Deporte"
    elif categoria == "3":
        return "Geografía"
    else:
        print("Selección inválida. Por favor, elige 1, 2 o 3.")
        return seleccionar_categoria()

# Función para jugar la trivia
def jugar_trivia():
    nombre = input("Ingresa tu nombre: ")
    categoria = seleccionar_categoria()
    preguntas_categoria = preguntas[categoria]
    puntuacion = 0

    num_preguntas = min(5, len(preguntas_categoria))

    for i in range(num_preguntas):
        pregunta_actual = preguntas_categoria[i]
        print(f"Pregunta {i + 1}: {pregunta_actual['pregunta']}")

        for i, opcion in enumerate(pregunta_actual['opciones']):
            print(f"{i + 1}. {opcion}")

        respuesta = input("Selecciona la opción correcta: ")

        if respuesta.isdigit() and 1 <= int(respuesta) <= len(pregunta_actual['opciones']):
            respuesta_seleccionada = pregunta_actual['opciones'][int(respuesta) - 1]
            if respuesta_seleccionada.lower() == pregunta_actual['respuesta'].lower():
                puntuacion += 3
                print("¡Correcto! +3 puntos")
            else:
                print(f"Incorrecto. La respuesta correcta era: {pregunta_actual['respuesta']}")
        else:
            print("Opción inválida. Por favor, elige un número.")

        print(f"Puntuación actual: {puntuacion}")
        print("")

    print(f"Juego terminado. Puntuación final: {puntuacion}")
    return nombre, puntuacion


# Ejecución del programa
bienvenida()
nombre, puntuacion = jugar_trivia()
