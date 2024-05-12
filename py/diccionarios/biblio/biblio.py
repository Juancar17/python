class Biblioteca():
    def __init__(self):
         self.libros = {}  # Inicializar un diccionario para almacenar los libros

    def agregarLibro(self):
        print("Agregando Libro")
        titulo = input("Ingrese el Titulo del libro: ")
        autor = input("Ingrese el Autor del libro: ")
        genero = input("Ingrese el Genero del libro: ")
        anio_publicacion = int(input("Ingrese el Año de Publicación: "))
        
        
        libro = {
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "anio_publicacion": anio_publicacion,
            "prestado": False
        }
        
        self.libros[titulo] = libro
        print("Libro agregado correctamente.")

    def mostrarLibros(self):
        if not self.libros:
            print("No hay ningun libro prestado")
        else:
            print("Libros prestados:\n")
            for titulo, info in self.libros.items():
                print(f"\nTítulo: {info['titulo']}")
                print(f"Autor: {info['autor']}")
                print(f"Género: {info['genero']}")
                print(f"Año de Publicación: {info['anio_publicacion']}")
                estado = "Prestado" if info['prestado'] else "Disponible"
                print(f"Estado: {estado}")
        
    def prestarLibro(self, titulo):
        if titulo in self.libros:
            if not self.libros[titulo]["prestado"]:
                self.libros[titulo]["prestado"] = True
                print(f"El libro '{titulo}' ha sido prestado correctamente.")
            else:
                print(f"El libro '{titulo}' ya está prestado.")
        else:
            print(f"No se encuentra el libro '{titulo}' en la biblioteca.")
    
    def devolverLibro(self, titulo):
        if titulo in self.libros:
            if self.libros[titulo]["prestado"]:
                self.libros[titulo]["prestado"] = False
                print(f"Se ha devuelto correctamente el libro '{titulo}'.")
            else:
                print(f"El libro '{titulo}' no está actualmente prestado.")
        else:
            print(f"No se encuentra el libro '{titulo}' en la biblioteca.")
            
    def main():
        print(" BIENVENO(A) Al PROGRAMA PRINCIPAL ")
        
        biblioteca = Biblioteca()

        while True:
            print("\n--- MENÚ PRINCIPAL ---")
            print("1. Agregar un libro")
            print("2. Mostrar todos los libros")
            print("3. Prestar un libro")
            print("4. Devolver un libro")
            print("5. Salir")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == '1':
                biblioteca.agregarLibro()
                libros=("Ingrese el título del libro a prestar: ")
            elif opcion == '2':
                biblioteca.mostrarLibros()
            elif opcion == '3':
                titulo = input("Ingrese el título del libro a prestar: ")
                biblioteca.prestarLibro(titulo)
            elif opcion == '4':
                titulo = input("Ingrese el título del libro a devolver: ")
                biblioteca.devolverLibro(titulo)
            elif opcion == '5':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    
    
if __name__ == '__main__':
    Biblioteca.main()