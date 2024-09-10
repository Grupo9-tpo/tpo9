'''Edits:
+Estructura dividida en FUNCION y PROGRAMA 
+Eliminacion de prints innecesarios dentro de la seccion FUNCION y adicion de returns
+Referencias y llamadas a las funciones dentro de la seccion de PROGRAMA
+Diccionarios de Entretenimiento y Deporte completos con una amplia selecc de pregs y rtas
'''

###FUNCION

#Funciones

# Función de bienvenida
def bienvenida():
    print("Bienvenido a Triviathon!")

# Función para seleccionar categoría
def seleccionar_categoria():
    print("Selecciona una categoría:")
    print("1. Entretenimiento")
    print("2. Deporte")

    categoria = input("Ingrese el número de la categoría que desea jugar: ")
    if categoria == "1":
        return "Entretenimiento"
    elif categoria == "2":
        return "Deporte"
    else:
        print("Selección inválida. Por favor, elige 1 o 2.")
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

        respuesta = input("Selecciona la opción correcta (1-4): ")

        if respuesta.isdigit() and 1 <= int(respuesta) <= len(pregunta_actual['opciones']):
            respuesta_seleccionada = pregunta_actual['opciones'][int(respuesta) - 1]
            if respuesta_seleccionada.lower() == pregunta_actual['respuesta'].lower():
                puntuacion += 3
                print("¡Correcto! +3 puntos")
            else:
                print(f"Incorrecto. La respuesta correcta era: {pregunta_actual['respuesta']}")
        else:
            print("Opción inválida. Por favor, elige un número entre 1 y 4.")

        print(f"Puntuación actual: {puntuacion}")
        print("")

    print(f"Juego terminado. Puntuación final: {puntuacion}")
    return nombre, puntuacion

# Diccionario de preguntas
preguntas = {
    "Entretenimiento": [
        {"pregunta": "¿En qué serie de televisión se encuentran los personajes principales Ross, Rachel, y Chandler?", 
        "opciones": ["The Office", "Suits", "Friends"], 
        "respuesta": "Friends"},
        {"pregunta": "¿En qué año se estrenó la primera temporada de 'Breaking Bad'?", 
        "opciones": ["2006", "2007", "2008", "2009"], 
        "respuesta": "2008"},
        {"pregunta": "¿Qué novela famosa fue escrita por George Orwell y publicada en 1949?", 
        "opciones": ["Fahrenheit 451", "1984", "Animal Farm"], 
        "respuesta": "1984"},
        {"pregunta": "¿De qué reconocida serie es la frase 'Winter is coming?'", 
        "opciones": ["Game of Thrones", "Snowpiercer", "The Walking Dead"], 
        "respuesta": "Game of Thrones"},
        {"pregunta": "En The Last of Us, ¿qué nombre tiene el personaje que es la protagonista femenina y que busca proteger a Ellie?", 
        "opciones": ["Sarah", "Tess", "Ellie"], 
        "respuesta": "Tess"}
    ],
    "Deporte": [
        {"pregunta": "¿Cuál es el club con más títulos de la Primera División de Argentina?", 
        "opciones": ["River Plate", "Boca Juniors", "Independiente"], 
        "respuesta": "River Plate"},
        {"pregunta": "¿Qué significa el término 'RM' en entrenamiento?", 
        "opciones": ["Repeticiones máximas", "Repeticiones medias", "Resistencia muscular"], 
        "respuesta": "Repeticiones máximas"},
        {"pregunta": "¿Cuál es el nombre del levantamiento que implica levantar la barra del suelo por encima de la cabeza en un solo movimiento?", 
        "opciones": ["Clean and Jerk", "Snatch", "Deadlift"], 
        "respuesta": "Snatch"},
        {"pregunta": "¿Quién es el máximo goleador histórico de Boca Juniors en torneos locales?", 
        "opciones": ["Martín Palermo", "Roberto Cherro", "Francisco Varallo", "Juan Román Riquelme"], 
        "respuesta": "Roberto Cherro"},
        {"pregunta": "¿Qué es un 'thruster' en CrossFit?", 
        "opciones": ["Un ejercicio isométrico para el core", "Un ejercicio cardiovascular de alta intensidad", "Un movimiento que combina una sentadilla frontal con un press de hombros"], 
        "respuesta": "Un movimiento que combina una sentadilla frontal con un press de hombros"}
    ],
    "Geografía": [
        {"pregunta": "¿Cuál es el país más grande del mundo por superficie?", 
        "opciones": ["China", "Rusia", "Canadá"], 
        "respuesta": "Rusia"},
        {"pregunta": "¿Cuál es el río más largo del mundo?", 
        "opciones": ["Nilo", "Amazonas", "Misisipi"], 
        "respuesta": "Amazonas"},
        {"pregunta": "¿En qué continente se encuentra el desierto del Sahara?", 
        "opciones": ["Asia", "África", "América del Sur"], 
        "respuesta": "África"},
        {"pregunta": "¿Qué país tiene la mayor cantidad de islas en el mundo?", 
        "opciones": ["Noruega", "Suecia", "Filipinas"], 
        "respuesta": "Suecia"},
        {"pregunta": "¿Cuál es la capital de Australia?", 
        "opciones": ["Sídney", "Melbourne", "Canberra"], 
        "respuesta": "Canberra"}
    ]
}

# Ejecución del programa
bienvenida()
nombre, puntuacion = jugar_trivia()
