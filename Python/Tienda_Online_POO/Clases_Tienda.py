class Producto:
    def __init__(self, nombre, precio, cantidad, categoria):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria

    def __str__(self):
        return f"{self.nombre} ({self.categoria}): ${self.precio} ({self.cantidad} disponibles)"

class Carrito:
    def __init__(self):
        self.productos = []
        self.total = 0

    def agregar_producto(self, producto, cantidad):
        if cantidad <= producto.cantidad:
            for i in range(cantidad):
                self.productos.append(producto)
            self.total += producto.precio * cantidad
            producto.cantidad -= cantidad
            print(f"Se han agregado {cantidad} unidades de {producto.nombre} al carrito.")
        else:
            print("No hay suficientes unidades disponibles en el inventario.")

    def quitar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
            self.total -= producto.precio
            producto.cantidad += 1
            print(f"Se ha eliminado {producto.nombre} del carrito.")
        else:
            print("El producto no está en el carrito.")

    def calcular_total(self):
        return self.total

    def ver_productos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("El carrito está vacío.")
