import unittest
from main import inicializar_archivo, guardar_puntaje, seleccionar_categoria

class TestTrivia(unittest.TestCase):
    def test_inicializar_archivo(self):
        # Verifica si el archivo de puntajes se crea correctamente
        inicializar_archivo()
        with open("puntajes.txt", "r") as archivo:
            contenido = archivo.read()
        self.assertEqual(contenido, "")

    def test_guardar_puntaje(self):
        # Verifica si el puntaje se guarda correctamente
        inicializar_archivo()  # Limpiar el archivo antes de guardar
        guardar_puntaje("TestUser", 10)
        
        with open("puntajes.txt", "r") as archivo:
            contenido = archivo.read()
        
        # Comprobar que el puntaje fue guardado correctamente
        self.assertIn("TestUser,10\n", contenido)

    def test_seleccionar_categoria(self):
        # Verifica que selecciona una categoría no jugada
        categorias_jugadas = ["Entretenimiento"]
        categoria = seleccionar_categoria(categorias_jugadas)
        
        # Asegura que la categoría seleccionada no esté en `categorias_jugadas`
        self.assertNotIn(categoria, categorias_jugadas)

if __name__ == "__main__":
    unittest.main()
