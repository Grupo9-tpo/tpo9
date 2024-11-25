import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import os
from preguntas import preguntas  # Import de preguntas.py

registro_puntajes = "puntajes.txt"

# Inicializar el archivo de puntajes si no existe
def inicializar_archivo():
    try:
        if not os.path.exists(registro_puntajes):
            with open(registro_puntajes, "w") as archivo:
                archivo.write("")  # Crear el archivo vacío si no existe
    except Exception as e:
        print(f"Error al inicializar el archivo de puntajes: {e}")

# Guardar el puntaje en un archivo
def guardar_puntaje(nombre, puntuacion):
    try:
        with open(registro_puntajes, "a") as archivo:
            archivo.write(f"{nombre},{puntuacion}\n")  # Guardar nombre y puntuación
    except Exception as e:
        print(f"Error al guardar el puntaje: {e}")

# Seleccionar categorías disponibles que no han sido jugadas aún
def seleccionar_categoria(categorias_jugadas):
    try:
        categorias_disponibles = [
            cat for cat in preguntas.keys() if cat not in categorias_jugadas
        ]
        return categorias_disponibles
    except Exception as e:
        print(f"Error al seleccionar las categorías: {e}")
        return []

# Crear botones para las categorías disponibles
def crear_botones_categoria(categorias_jugadas, categorias_frame, puntos_label, nombre_jugador, puntos):
    categorias_disponibles = seleccionar_categoria(categorias_jugadas)
    if not categorias_disponibles:
        messagebox.showinfo("Fin del juego", "¡Has jugado todas las categorías!")
        finalizar_juego(nombre_jugador, puntos)  # Finalizar al terminar todas las categorías
        return

    # Limpiar los botones anteriores
    for widget in categorias_frame.winfo_children():
        widget.destroy()

    # Crear botones para las categorías disponibles
    for categoria in categorias_disponibles:
        btn = tk.Button(categorias_frame, text=categoria, command=lambda cat=categoria: abrir_ventana_trivia(cat, categorias_jugadas, categorias_frame, puntos_label, nombre_jugador, puntos))
        btn.pack(pady=5)

    # Botón para salir
    salir_btn = tk.Button(categorias_frame, text="Salir", command=lambda: salir_del_juego(nombre_jugador, puntos))
    salir_btn.pack(pady=10)

# Iniciar el juego de trivia con preguntas aleatorias
def iniciar_trivia(categoria, categorias_jugadas, categorias_frame, puntos_label, nombre_jugador, puntos):
    try:
        preguntas_categoria = preguntas[categoria]
        random.shuffle(preguntas_categoria)
        preguntas_a_jugar = preguntas_categoria[:5]  # Seleccionar 5 preguntas aleatorias
        indice_pregunta = 0

        # Crear un label para mostrar las preguntas
        pregunta_label = tk.Label(categorias_frame, text="", font=("Arial", 12), wraplength=300)
        pregunta_label.grid(row=0, column=0, pady=10)

        # Frame para las opciones de respuesta
        opciones_frame = tk.Frame(categorias_frame)
        opciones_frame.grid(row=1, column=0, pady=10)

        # Función para avanzar a la siguiente pregunta
        def siguiente_pregunta():
            nonlocal puntos, indice_pregunta
            if indice_pregunta >= len(preguntas_a_jugar):
                # Ya se jugaron las 5 preguntas
                categorias_jugadas.append(categoria)
                messagebox.showinfo("Fin de la categoría", "¡Has terminado esta categoría!")
                crear_botones_categoria(categorias_jugadas, categorias_frame, puntos_label, nombre_jugador, puntos)  # Actualizar las opciones de categorías
                return

            pregunta_actual = preguntas_a_jugar[indice_pregunta]
            pregunta_label.config(text=pregunta_actual['pregunta'])

            # Limpiar las opciones previas
            for widget in opciones_frame.winfo_children():
                widget.destroy()

            for i, opcion in enumerate(pregunta_actual['opciones']):
                btn = tk.Button(opciones_frame, text=opcion, command=lambda seleccion=opcion, respuesta=pregunta_actual['respuesta']: verificar_respuesta(seleccion, respuesta))
                btn.grid(row=i, column=0, padx=10, pady=5)

        # Verificar si la respuesta es correcta
        def verificar_respuesta(seleccion, respuesta_correcta):
            nonlocal puntos, indice_pregunta
            if seleccion.lower() == respuesta_correcta.lower():
                puntos += 3
                messagebox.showinfo("Respuesta correcta", f"¡Correcto! +3 puntos.")
            else:
                messagebox.showinfo("Respuesta incorrecta", f"Incorrecto. La respuesta correcta era: {respuesta_correcta}")

            puntos_label.config(text=f"Puntos: {puntos}")  # Actualizar los puntos
            indice_pregunta += 1  # Avanzar al siguiente índice de pregunta
            siguiente_pregunta()  # Mostrar la siguiente pregunta

        siguiente_pregunta()
    except KeyError as e:
        print(f"Error: No se encontraron preguntas para la categoría {categoria}: {e}")
    except Exception as e:
        print(f"Error al iniciar la trivia: {e}")

# Obtener el nombre del jugador
def obtener_nombre():
    try:
        nombre = simpledialog.askstring("Nombre del jugador", "¿Cuál es tu nombre?")
        return nombre if nombre else "Jugador"
    except Exception as e:
        print(f"Error al obtener el nombre del jugador: {e}")
        return "Jugador"

# Salir del juego y guardar los puntajes
def salir_del_juego(nombre_jugador, puntos_totales):
    try:
        respuesta = messagebox.askyesno("Salir", "¿Estás seguro que deseas salir?")
        if respuesta:
            guardar_puntaje(nombre_jugador, puntos_totales)
            messagebox.showinfo("Juego Terminado", f"¡Juego finalizado! Puntuación total: {puntos_totales}")
            ventana_principal.quit()  # Cerrar la ventana principal
    except Exception as e:
        print(f"Error al intentar salir del juego: {e}")

# Finalizar el juego y guardar los puntajes
def finalizar_juego(nombre_jugador, puntos_totales):
    try:
        guardar_puntaje(nombre_jugador, puntos_totales)
        messagebox.showinfo("Juego Terminado", f"¡Juego finalizado! Puntuación total: {puntos_totales}")
        ventana_principal.quit()  # Cerrar la ventana principal
    except Exception as e:
        print(f"Error al finalizar el juego: {e}")

# Iniciar el juego
def iniciar_juego():
    # Aquí no es necesario el `try/except` porque este flujo es controlado
    inicializar_archivo()
    categorias_jugadas = []
    nombre = obtener_nombre()  # Pedir el nombre al iniciar el juego
    puntos = 0  # Inicializar los puntos fuera de las funciones

    # Crear la ventana principal
    global ventana_principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Triviathon")
    ventana_principal.geometry("400x400")  # Tamaño de la ventana

    # Etiqueta para instrucciones
    instrucciones_label = tk.Label(ventana_principal, text="Bienvenido a Triviathon", font=("Arial", 14))
    instrucciones_label.pack(pady=20)

    # Frame para las categorías
    categorias_frame = tk.Frame(ventana_principal)
    categorias_frame.pack(pady=10)

    # Etiqueta para los puntos
    puntos_label = tk.Label(ventana_principal, text=f"Puntos: {puntos}", font=("Arial", 12))
    puntos_label.pack()

    # Crear botones para seleccionar categorías
    crear_botones_categoria(categorias_jugadas, categorias_frame, puntos_label, nombre, puntos)  # Crear los botones para seleccionar categorías

    ventana_principal.mainloop()

# Abrir la ventana de trivia para una categoría seleccionada
def abrir_ventana_trivia(categoria, categorias_jugadas, categorias_frame, puntos_label, nombre_jugador, puntos):
    # Aquí se hace la lógica sin `try/except` para controlar el flujo en la interfaz
    for widget in categorias_frame.winfo_children():
        widget.destroy()

    iniciar_trivia(categoria, categorias_jugadas, categorias_frame, puntos_label, nombre_jugador, puntos)

# Iniciar el juego cuando la ventana se ejecute
if __name__ == "__main__":
    iniciar_juego()
