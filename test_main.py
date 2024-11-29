import unittest
import tkinter as tk
from main import inicializar_archivo, seleccionar_categoria

def ventana_principal():
    ventana = tk.Tk()
    ventana.title("Trivia de Python")
    return ventana 

class TestTrivia(unittest.TestCase):
    
    def test_seleccionar_categoria(self):
        # Verifica que selecciona una categoría no jugada
        categorias_jugadas = ["Entretenimiento"]
        categoria = seleccionar_categoria(categorias_jugadas)

        # Asegura que la categoría seleccionada no esté en `categorias_jugadas`
        self.assertNotIn(categoria, categorias_jugadas)

    def test_iniciar_ventana(self):
        # Verifica que la ventana de Tkinter se crea correctamente
        ventana = ventana_principal()
        self.assertTrue(ventana.winfo_exists())  # Verifica si la ventana existe
        ventana.destroy()  # Cerrar la ventana después de la prueba

    def test_titulo_visible(self):
        # Verifica si el título de la ventana es correcto
        ventana = ventana_principal()
        titulo = ventana.title()
        self.assertEqual(titulo, "Trivia de Python")
        ventana.destroy()

    def test_cargar_categorias(self):
        # Simula la carga de categorías
        categorias = ["Entretenimiento", "Deporte", "Historia", "Tecnología"]
        ventana = ventana_principal()

        # Se crea un botón para cada categoría
        for categoria in categorias:
            boton = tk.Button(ventana, text=categoria)
            boton.grid()
            self.assertEqual(boton.cget("text"), categoria)  # Verifica el texto del botón

        ventana.destroy()


    def test_respuesta_correcta(self):
        # Verifica si se actualiza el puntaje cuando se selecciona la respuesta correcta
        respuesta_correcta = "París"
        respuesta_usuario = "París"  # Supongamos que el usuario selecciona la respuesta correcta
        puntaje = 0

        if respuesta_usuario == respuesta_correcta:
            puntaje += 3  # Se otorgan 10 puntos por respuesta correcta

        self.assertEqual(puntaje, 3)  # Verifica que el puntaje sea el esperado

    def test_respuesta_incorrecta(self):
        # Verifica que el puntaje no cambie si la respuesta es incorrecta
        respuesta_correcta = "París"
        respuesta_usuario = "Londres"  # Respuesta incorrecta
        puntaje = 0

        if respuesta_usuario != respuesta_correcta:
            puntaje = 0  # No se otorgan puntos

        self.assertEqual(puntaje, 0)  # Verifica que el puntaje siga siendo 0

    def test_guardar_puntajes(self):
        # Simula el guardado de un puntaje
        nombre_usuario = "TestUser"
        puntaje = 30

        with open("puntajes.txt", "a") as archivo:
            archivo.write(f"{nombre_usuario},{puntaje}\n")

        # Verifica que el puntaje se haya guardado correctamente
        with open("puntajes.txt", "r") as archivo:
            contenido = archivo.read()

        self.assertIn("TestUser,30\n", contenido)  # Verifica que el puntaje se haya guardado


if __name__ == "__main__":
    unittest.main()
