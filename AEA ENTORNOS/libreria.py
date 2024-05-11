import json

class Libreria:
    def __init__(self):
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        self.libros.append({'titulo': titulo, 'autor': autor, 'genero': genero, 'anio': anio})
        return "Libro añadido"

    def buscar_libro(self, titulo):
        return [libro for libro in self.libros if libro['titulo'].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros if autor.lower() in libro['autor'].lower()]

    def eliminar_libro(self, titulo):
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if libro['titulo'].lower() != titulo.lower()]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"

    def guardar_libros(self, archivo):
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
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


"""
1: Reformatear el código según PEP 8 y PEP 257

Asegurar que todo el código cumpla con las directrices de estilo de PEP 8 para mejorar la legibilidad y el mantenimiento del código.
Documentar todas las clases y métodos siguiendo las convenciones de PEP 257, proporcionando descripciones claras y concisas de su funcionamiento.
"""

import json

class Libreria:
    """
    Clase que representa una librería que puede almacenar y manipular libros.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de Libreria con una lista vacía de libros.
        """
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        """
        Añade un nuevo libro a la librería.

        Args:
            titulo (str): Título del libro.
            autor (str): Nombre del autor del libro.
            genero (str): Género del libro.
            anio (int): Año de publicación del libro.

        Returns:
            str: Mensaje indicando que el libro fue añadido.
        """
        self.libros.append({'titulo': titulo, 'autor': autor, 'genero': genero, 'anio': anio})
        return "Libro añadido"

    def buscar_libro(self, titulo):
        """
        Busca un libro por su título en la librería.

        Args:
            titulo (str): Título del libro a buscar.

        Returns:
            list: Lista de libros que coinciden con el título (puede estar vacía).
        """
        return [libro for libro in self.libros if libro['titulo'].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        """
        Busca libros por un autor específico en la librería.

        Args:
            autor (str): Nombre del autor a buscar.

        Returns:
            list: Lista de libros escritos por el autor (puede estar vacía).
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
        Guarda la lista de libros en un archivo JSON.

        Args:
            archivo (str): Nombre del archivo donde se guardará la información.

        Returns:
            str: Mensaje indicando que los libros fueron guardados.
        """
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
        """
        Carga la lista de libros desde un archivo JSON.

        Args:
            archivo (str): Nombre del archivo desde donde se cargarán los libros.

        Returns:
            str: Mensaje indicando que los libros fueron cargados o si el archivo no fue encontrado.
        """
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"


# Ejemplo de uso
mi_libreria = Libreria()
mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
mi_libreria.guardar_libros('libreria.json')
print(mi_libreria.cargar_libros('libreria.json'))
print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))

