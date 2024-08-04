
from libro import Libro

class GestionBiblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        if isinstance(libro, Libro):
            self.libros.append(libro)
        else:
            print("Error: El objeto no es una instancia de la clase Libro.")

    def listar_libros(self):
        if self.libros:
            for libro in self.libros:
                print(libro)
        else:
            print("No hay libros en la biblioteca.")

    def buscar_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros if libro.titulo.lower() == titulo.lower()]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con ese título.")

    def buscar_por_autor(self, autor):
        resultados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros de ese autor.")
