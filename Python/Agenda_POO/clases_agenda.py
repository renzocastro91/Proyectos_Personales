#Clases utilizadas para el programa

class Contacto:
    def __init__(self,codigo,nombre,telefono1,telefono2,direccion):
        self.codigo = codigo
        self.nombre = nombre
        self.telefono1 = telefono1
        self.telefono2 = telefono2
        self.direccion = direccion

    def descripcion(self):
        return f"Contacto: {self.nombre} Teléfono 1: {self.telefono1} Teléfono 2: {self.telefono2} Dirección: {self.direccion}"

    def descripcion_dev(self):
        return f"Indice : {self.codigo} Contacto: {self.nombre}"

    def cambiar_nombre(self,nuevo):
        self.nombre = nuevo
    
    def cambiar_telefono1(self,nuevo):
        self.telefono1 = nuevo

    def cambiar_telefono2(self,nuevo):
        self.telefono2 = nuevo

    def cambiar_direccion(self,nuevo):
        self.direccion = nuevo

    def cambiar_codigo(self,nuevo):
        self.codigo = nuevo
    
    def devolver_atributos(self):
        return [self.codigo,self.nombre,self.telefono1,self.telefono2,self.direccion]