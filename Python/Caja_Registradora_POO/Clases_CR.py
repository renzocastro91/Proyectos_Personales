#Aquí estarán todas las clases utilizadas en el programa

class Articulo:
    def __init__(self,cod,nom,marc,pre,sto):
        self.codigo = cod
        self.nombre = nom
        self.marca = marc
        self.precio = pre
        self.stock = sto

    def descripcion(self):
       print(f"Codigo Producto = {self.codigo} / Artículo: {self.nombre} / Marca: {self.marca} / Precio: {self.precio} / Stock: {self.stock}")

    def devolver_atributos(self):
        return [self.codigo,self.nombre,self.marca,self.precio,self.stock]
    
    def cambiarstock(self,cantidad):
        self.stock = self.stock - cantidad

    def modificar_nombre(self,nuevo):
        self.nombre = nuevo
    
    def modificar_marca(self,nuevo):
        self.marca = nuevo
    
    def modificar_precio(self,nuevo):
        self.precio = nuevo
    
    def modificar_stock(self,nuevo):
        self.stock = nuevo

class Carrito:
    def __init__(self,numero,mon):
        self.cant_arti = numero
        self.monto_tot = mon

    def descripcion(self):
        return f"Cantidad de artículos comprados {self.cant_arti} y Total a pagar: ${self.monto_tot}"
        
class Registro_compra:
    def __init__(self,codigo,monto_acu,fecha): 
        self.codigo = codigo
        self.monto_acu = monto_acu
        self.fecha = fecha
    
    def devolver_atributos(self):
        return [self.codigo,self.monto_acu,self.fecha]