
"""
Objetivo: Desarrollar y mejorar un sistema de gestión de librería virtual en Python que permita a los usuarios 
realizar operaciones como añadir, buscar, modificar, y eliminar libros, así 
como guardar y cargar la colección desde un archivo. El código deberá seguir las mejores
prácticas de programación, ser completamente funcional y estar bien documentado.

1: Reformatear el código según PEP 8 y PEP 257

Asegurar que todo el código cumpla con las directrices de estilo de PEP 8 para mejorar la legibilidad y el mantenimiento del código.
Documentar todas las clases y métodos siguiendo las convenciones de PEP 257, proporcionando descripciones claras y concisas de su funcionamiento.


2: Escribir test unitarios
Desarrollar un conjunto completo de pruebas unitarias utilizando el módulo unittest de Python para verificar la funcionalidad de cada método en la clase de gestión de la librería.
Asegurar que las pruebas cubran casos de uso típicos así como casos extremos y errores de entrada.
Ejecutar las pruebas para validar la integridad del código y asegurar que no existen regresiones después de cambios o mejoras.
Opcional: Codificar un método nuevo en el código fuente original y realizar un test unitario diferente a los otros realizados sobre los métodos ya implementados en el código original. 

3: Debugging
Utilizar las herramientas de debugging integradas en un IDE como PyCharm o Visual Studio Code para identificar y resolver errores.
Practicar la colocación de puntos de interrupción y el seguimiento paso a paso del código para entender cómo las diferentes partes del programa interactúan.
Documentar los problemas encontrados y cómo se solucionaron, proporcionando una visión valiosa sobre el proceso de debugging.

4: Control de versiones con GitHub
Aprender los fundamentos del uso de Git para el control de versiones, incluyendo la creación de repositorios, el seguimiento de archivos, la realización de commits y la sincronización con GitHub.
Organizar el código en un repositorio de GitHub, asegurándose de que el repositorio contenga un README adecuado, comentarios en los commits que expliquen los cambios realizados y una estructura de directorios lógica.
Practicar la colaboración y el mantenimiento de un historial de cambios claro y útil.
"""
import json


class Libreria:
    """
    Clase para gestionar una librería virtual.
    """

    def __init__(self):
        """
        Inicializa la librería con una lista vacía de libros.
        """
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        """
        Añade un libro a la librería.

        Args:
            titulo (str): Título del libro.
            autor (str): Autor del libro.
            genero (str): Género del libro.
            anio (int): Año de publicación del libro.

        Returns:
            str: Mensaje indicando que el libro ha sido añadido.
        """
        self.libros.append({'titulo': titulo, 'autor': autor, 'genero': genero, 'anio': anio})
        return "Libro añadido"

    def buscar_libro(self, titulo):
        """
        Busca un libro por su título.

        Args:
            titulo (str): Título del libro a buscar.

        Returns:
            list: Lista de libros que coinciden con el título (puede ser vacía).
        """
        return [libro for libro in self.libros if libro['titulo'].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        """
        Busca libros por el nombre del autor.

        Args:
            autor (str): Nombre del autor a buscar.

        Returns:
            list: Lista de libros escritos por el autor especificado.
        """
        return [libro for libro in self.libros if autor.lower() in libro['autor'].lower()]

    def eliminar_libro(self, titulo):
        """
        Elimina un libro de la librería por su título.

        Args:
            titulo (str): Título del libro a eliminar.

        Returns:
            str: Mensaje indicando si el libro fue eliminado o no encontrado.
        """
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if libro['titulo'].lower() != titulo.lower()]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"

    def guardar_libros(self, archivo):
        """
        Guarda la colección de libros en un archivo JSON.

        Args:
            archivo (str): Nombre del archivo JSON donde se guardarán los libros.

        Returns:
            str: Mensaje indicando que los libros han sido guardados.
        """
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
        """
        Carga la colección de libros desde un archivo JSON.

        Args:
            archivo (str): Nombre del archivo JSON desde donde cargar los libros.

        Returns:
            str: Mensaje indicando que los libros han sido cargados o si el archivo no fue encontrado.
        """
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"


mi_libreria = Libreria()
mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
mi_libreria.guardar_libros('libreria.json')
print(mi_libreria.cargar_libros('libreria.json'))
print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))



import unittest

class TestLibreria(unittest.TestCase):

    def setUp(self):
        self.libreria = Libreria()
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)

    def test_anadir_libro(self):
        self.assertEqual(self.libreria.anadir_libro("1984", "George Orwell", "Ciencia Ficción", 1949), "Libro añadido")

    def test_buscar_libro(self):
        self.assertEqual(self.libreria.buscar_libro("Cien años de soledad"), [{'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'genero': 'Novela', 'anio': 1967}])

    def test_buscar_por_autor(self):
        self.assertEqual(self.libreria.buscar_por_autor("Gabriel García Márquez"), [{'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'genero': 'Novela', 'anio': 1967}])

    def test_eliminar_libro(self):
        self.assertEqual(self.libreria.eliminar_libro("Cien años de soledad"), "Libro eliminado")
        self.assertEqual(self.libreria.eliminar_libro("1984"), "Libro no encontrado")

    def test_guardar_y_cargar_libros(self):
        self.assertEqual(self.libreria.guardar_libros('test_libreria.json'), "Libros guardados")
        self.assertEqual(self.libreria.cargar_libros('test_libreria.json'), "Libros cargados")
        self.assertEqual(len(self.libreria.libros), 1)  # Comprobar que se cargó un libro correctamente

if __name__ == '__main__':
    unittest.main()
