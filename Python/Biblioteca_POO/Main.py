from Clases import *

biblioteca = Biblioteca("Biblioteca Nacional")

biblioteca.agregar_libro("Cien años de soledad", "Gabriel García Márquez", 1967, 471)
biblioteca.agregar_libro("El Aleph", "Jorge Luis Borges", 1949, 160)
biblioteca.agregar_libro("La casa de los espíritus", "Isabel Allende", 1982, 368)

biblioteca.consultar_catalogo()

biblioteca.prestar_libro("Cien años de soledad", "Juan Pérez")

biblioteca.consultar_prestamos()

biblioteca.devolver_libro("Cien años de soledad")

biblioteca.consultar_prestamos()

biblioteca.consultar_libro("El Aleph")

print("===============================")


# Bucle para leer todo lo cargado
for libro in biblioteca.catalogo:
    print(libro.titulo)
    print(libro.autor)
    print(libro.publicacion)
    print(libro.paginas)
    print("=================")
