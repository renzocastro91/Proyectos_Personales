class Empleado:
    def __init__(self, nombre, identificacion, salario_base, posicion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.salario_base = salario_base
        self.posicion = posicion
        self.bonificaciones = 0
        self.horario = ""

    def asignar_bonificacion(self, bonificacion):
        self.bonificaciones = bonificacion

    def asignar_horario(self, horario):
        self.horario = horario

    def calcular_salario_total(self):
        salario_total = self.salario_base + self.bonificaciones
        if self.horario == "tiempo completo":
            salario_total *= 1.5
        elif self.horario == "medio tiempo":
            salario_total *= 0.75
        return salario_total

    def obtener_informacion(self):
        print("Nombre:", self.nombre)
        print("Identificación:", self.identificacion)
        print("Posición:", self.posicion)
        print("Salario base:", self.salario_base)
        print("Bonificaciones:", self.bonificaciones)
        print("Horario:", self.horario)

    def modificar_posicion(self, nueva_posicion):
        self.posicion = nueva_posicion

    def eliminar_empleado(self):
        del self

