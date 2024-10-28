# Importar los diccionarios desde preguntas.py
import random
from preguntas import preguntas

# Función de bienvenida
def bienvenida():
    print("¡Bienvenido a Triviathon!")

# Función para seleccionar categoría aleatoria, excluyendo las ya jugadas
def seleccionar_categoria(categorias_jugadas):
    categorias_disponibles = [categoria for categoria in preguntas.keys() if categoria not in categorias_jugadas]
    return random.choice(categorias_disponibles)  # Selecciona una categoría aleatoria de las no jugadas

# Función para jugar la trivia
def jugar_trivia(categorias_jugadas):
    nombre = input("Ingresa tu nombre: ") if not categorias_jugadas else None  # Pregunta el nombre solo al inicio
    
    # Selecciona una categoría aleatoria que no se haya jugado
    categoria = seleccionar_categoria(categorias_jugadas)
    print(f"Se ha seleccionado la categoría: {categoria}")
    
    preguntas_categoria = preguntas[categoria]
    
    # Mezcla las preguntas de la categoría seleccionada
    random.shuffle(preguntas_categoria)

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

    return categoria, puntuacion

# Función principal del programa
def main():
    bienvenida()
    categorias_jugadas = []
    historial_puntos = []
    
    while len(categorias_jugadas) < 3:
        # Jugar trivia y obtener la categoría jugada y los puntos obtenidos
        categoria, puntos = jugar_trivia(categorias_jugadas)
        
        # Guardar la categoría y los puntos en el historial
        categorias_jugadas.append(categoria)
        historial_puntos.append((categoria, puntos))
        
        # Si se han jugado 3 categorías, finalizar automáticamente
        if len(categorias_jugadas) == 3:
            print("\n¡Has jugado las 3 categorías! Fin del juego.")
            break
        
        # Preguntar si el jugador desea continuar o finalizar
        continuar = input("¿Deseas seguir jugando? (s/n): ").lower()
        if continuar != 's':
            print("\nHas decidido finalizar el juego.")
            break
    
    # Imprimir el historial de puntos
    print("\nHistorial de puntos:")
    for categoria, puntos in historial_puntos:
        print(f"Categoría: {categoria}, Puntos: {puntos}")
    
    print(f"\nPuntuación total: {sum(puntos for _, puntos in historial_puntos)}")

# Ejecución del programa
main()
