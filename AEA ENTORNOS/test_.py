"""
2: Escribir test unitarios

Desarrollar un conjunto completo de pruebas unitarias utilizando el módulo unittest de Python para verificar la funcionalidad de cada método en la clase de gestión de la librería.
Asegurar que las pruebas cubran casos de uso típicos así como casos extremos y errores de entrada.
Ejecutar las pruebas para validar la integridad del código y asegurar que no existen regresiones después de cambios o mejoras.
Opcional: Codificar un método nuevo en el código fuente original y realizar un test unitario diferente a los otros realizados sobre los métodos ya implementados en el código original. 
"""

import unittest
import json
from libreria import Libreria  # Asumiendo que el código está en un archivo llamado libreria.py

class TestLibreria(unittest.TestCase):
    def setUp(self):
        # Configuración inicial para cada prueba
        self.libreria = Libreria()

    def tearDown(self):
        # Limpiar después de cada prueba si es necesario
        pass

    def test_anadir_libro(self):
        self.assertEqual(self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967), "Libro añadido")
        self.assertEqual(len(self.libreria.libros), 1)

    def test_buscar_libro(self):
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.assertEqual(len(self.libreria.buscar_libro("cien años de soledad")), 1)
        self.assertEqual(len(self.libreria.buscar_libro("no existe")), 0)

    def test_buscar_por_autor(self):
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.assertEqual(len(self.libreria.buscar_por_autor("garcía")), 1)
        self.assertEqual(len(self.libreria.buscar_por_autor("Orwell")), 0)

    def test_eliminar_libro(self):
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.assertEqual(self.libreria.eliminar_libro("cien años de soledad"), "Libro eliminado")
        self.assertEqual(len(self.libreria.libros), 0)
        self.assertEqual(self.libreria.eliminar_libro("no existe"), "Libro no encontrado")

    def test_guardar_cargar_libros(self):
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.assertEqual(self.libreria.guardar_libros('test_libreria.json'), "Libros guardados")
        self.assertEqual(self.libreria.cargar_libros('test_libreria.json'), "Libros cargados")
        self.assertEqual(len(self.libreria.libros), 1)

    def test_cargar_libros_no_existente(self):
        self.assertEqual(self.libreria.cargar_libros('archivo_inexistente.json'), "Archivo no encontrado")

if __name__ == '__main__':
    unittest.main()

