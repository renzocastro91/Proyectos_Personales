"""
Cines
Un complejo de cines está integrado por varios cines ubicados principalmente en los centros comerciales de la ciudad. 

Cada cine cuenta con una cantidad de salas, que son las que exhiben las películas en las distintas funciones cinematográficas. 

La programación de las salas se renueva en forma semanal, existiendo la posibilidad de que algunas salas queden sin uso. Cabe 
mencionar que no todas las salas tienen la misma capacidad (cantidad de butacas). La programación es la que determina qué películas 
van a proyectarse y los horarios para cada función de cada una de las salas, para todos los cines. Esta programación se realiza en forma 
centralizada, desde la administración del Complejo, tomándose como base la información de las películas próximas a estrenar, que envía el 
INCAA (Instituto Nacional de Cines y Artes Audiovisuales). 

La programación implica el diseño de las funciones y sus horarios en forma anticipada, debiendo el responsable de la misma, habilitar cada función 
en el momento que desee permitir la reserva y/o venta de entradas para la misma. La entrada que se le entrega al cliente representa el comprobante 
de venta y como tal debe cumplir con lo reglamentado en la Ley de Facturación vigente, debiendo contener como datos: nro. de venta, fecha de venta, 
número de función, sala en la que se proyecta la película, el nombre de la película, fecha y hora de la función, el precio, el tipo de entrada (si es mayor, 
menor, jubilado) y la calificación de la película, que según especificaciones de la Ley de Cine Nro. 17.741, debe ser informada tanto en la entrada como al 
inicio de la película. 

Es importante destacar que la entrada es válida únicamente para la fecha, hora y función indicadas en la misma. Los tipos de entradas y los días y horarios de 
proyección son los que determinan el precio de la entrada, que también pueden variar en cada cine del complejo. 

Las funciones admiten ciertos tipos de entradas y otros no, dependiendo de factores como: horarios, calificación de las películas, etc. Por ejemplo: si una 
película está calificada como para mayores de 16 años, para esa función no se pueden vender entradas de TIPO = MENOR. Cada función tiene asociado un tipo de función, 
que determina si la función es un preestreno, un estreno, una función normal. 
"""

import datetime

class Cine:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.salas = []

    def agregar_sala(self, sala):
        self.salas.append(sala)

    def eliminar_sala(self, sala):
        self.salas.remove(sala)


class Sala:
    def __init__(self, capacidad, numero, cine):
        self.capacidad = capacidad
        self.numero = numero
        self.cine = cine
        self.funciones = []

    def agregar_funcion(self, funcion):
        self.funciones.append(funcion)

    def eliminar_funcion(self, funcion):
        self.funciones.remove(funcion)


class Funcion:
    def __init__(self, pelicula, sala, horario_inicio, tipo):
        self.pelicula = pelicula
        self.sala = sala
        self.horario_inicio = horario_inicio
        self.tipo = tipo
        self.entradas_vendidas = []

    def vender_entrada(self, entrada):
        if entrada.tipo not in self.tipo_entradas_validas():
            raise ValueError("Este tipo de entrada no es válido para esta función")
        if len(self.entradas_vendidas) >= self.sala.capacidad:
            raise ValueError("No hay suficientes asientos disponibles")
        self.entradas_vendidas.append(entrada)

    def tipo_entradas_validas(self):
        if self.pelicula.edad_minima == 0:
            return ["MAYOR", "MENOR", "JUBILADO"]
        elif self.pelicula.edad_minima >= 16:
            return ["MAYOR", "JUBILADO"]
        else:
            return ["MAYOR", "MENOR", "JUBILADO"]


class Pelicula:
    def __init__(self, titulo, duracion, director, actores, edad_minima):
        self.titulo = titulo
        self.duracion = duracion
        self.director = director
        self.actores = actores
        self.edad_minima = edad_minima


# Definir los cines
cine1 = Cine("CinePlanet", "Av. Siempreviva 123", "01-2345678", 10)
cine2 = Cine("Cinemark", "Av. Revolución 456", "01-9876543", 8)
cine3 = Cine("Cinepolis", "Av. Insurgentes 789", "01-5432167", 12)

# Definir las películas
pelicula1 = Pelicula("Matrix 4", "Ciencia Ficción", "2:30")
pelicula2 = Pelicula("Rápidos y Furiosos 10", "Acción", "2:10")
pelicula3 = Pelicula("Spider-Man: Sin Camino a Casa", "Acción", "2:20")
pelicula4 = Pelicula("Jurassic World: Dominion", "Ciencia Ficción", "2:40")

# Asignar películas a los cines
cine1.agregar_pelicula(pelicula1)
cine1.agregar_pelicula(pelicula2)
cine2.agregar_pelicula(pelicula2)
cine2.agregar_pelicula(pelicula3)
cine3.agregar_pelicula(pelicula1)
cine3.agregar_pelicula(pelicula4)

# Imprimir la cartelera de cada cine
print("Cartelera de " + cine1.nombre)
print(cine1.obtener_cartelera())

print("Cartelera de " + cine2.nombre)
print(cine2.obtener_cartelera())

print("Cartelera de " + cine3.nombre)
print(cine3.obtener_cartelera())

# Comprar entradas
cliente1 = Cliente("Juan Pérez", "juan.perez@gmail.com", "01-1234567")
cliente2 = Cliente("María Gómez", "maria.gomez@gmail.com", "01-7654321")

print(cliente1.comprar_entrada(cine1, pelicula1, "2:30", "Normal", "Mayor"))
print(cliente2.comprar_entrada(cine2, pelicula3, "4:00", "Estreno", "Jubilado"))

# Imprimir las ventas totales de cada cine
print("Ventas totales de " + cine1.nombre + ": $" + str(cine1.obtener_ventas_totales()))
print("Ventas totales de " + cine2.nombre + ": $" + str(cine2.obtener_ventas_totales()))
print("Ventas totales de " + cine3.nombre + ": $" + str(cine3.obtener_ventas_totales()))
