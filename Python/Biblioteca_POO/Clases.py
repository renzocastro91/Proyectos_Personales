class Libro:
    def __init__(self, titulo, autor, publicacion, paginas, estado='disponible'):
        self.titulo = titulo
        self.autor = autor
        self.publicacion = publicacion
        self.paginas = paginas
        self.estado = estado
        
    def __str__(self):
        return f"{self.titulo} de {self.autor}, publicado en {self.publicacion}. {self.paginas} páginas. Estado: {self.estado}"
        

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []
        self.prestamos = {}
    
    def __str__(self):
        return f"Biblioteca {self.nombre}"
    
    def agregar_libro(self, titulo, autor, publicacion, paginas):
        libro = Libro(titulo, autor, publicacion, paginas)
        self.catalogo.append(libro)
        print(f"{libro} agregado a la biblioteca.")
    
    def consultar_catalogo(self):
        print("Catálogo de la biblioteca:")
        for libro in self.catalogo:
            print(libro)
    
    def consultar_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo == titulo:
                print(libro)
                return
        print(f"No se encontró el libro {titulo} en la biblioteca.")
    
    def prestar_libro(self, titulo, usuario):
        for libro in self.catalogo:
            if libro.titulo == titulo:
                if libro.estado == 'prestado':
                    print(f"Lo siento, el libro {titulo} ya está prestado.")
                else:
                    libro.estado = 'prestado'
                    self.prestamos[titulo] = usuario
                    print(f"El libro {titulo} ha sido prestado a {usuario}.")
                return
        print(f"No se encontró el libro {titulo} en la biblioteca.")
    
    def devolver_libro(self, titulo):
        if titulo in self.prestamos:
            usuario = self.prestamos.pop(titulo)
            for libro in self.catalogo:
                if libro.titulo == titulo:
                    libro.estado = 'disponible'
                    print(f"El libro {titulo} ha sido devuelto por {usuario}.")
                    return
        print(f"No se encontró el libro {titulo} en los préstamos.")
    
    def consultar_prestamos(self):
        if len(self.prestamos) == 0:
            print("No hay libros prestados en la biblioteca.")
        else:
            print("Libros prestados:")
            for titulo, usuario in self.prestamos.items():
                print(f"{titulo} prestado a {usuario}.")
