# main.py

from gestion import GestionBiblioteca
from libro import Libro

def menu():
    biblioteca = GestionBiblioteca()
    
    while True:
        print("\nGestión de Biblioteca")
        print("1. Agregar un libro")
        print("2. Listar libros")
        print("3. Buscar libro por título")
        print("4. Buscar libro por autor")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, isbn)
            biblioteca.agregar_libro(libro)
            print("Libro agregado exitosamente.")

        elif opcion == '2':
            biblioteca.listar_libros()

        elif opcion == '3':
            titulo = input("Ingrese el título del libro a buscar: ")
            biblioteca.buscar_por_titulo(titulo)

        elif opcion == '4':
            autor = input("Ingrese el autor del libro a buscar: ")
            biblioteca.buscar_por_autor(autor)

        elif opcion == '5':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    menu()
