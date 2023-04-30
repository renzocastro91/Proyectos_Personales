from Clases_Tienda import *

producto1 = Producto("Laptop Dell", 1000, 10, "Electrónica")
producto2 = Producto("Sofá de cuero", 500, 5, "Hogar")


# Creamos un objeto Carrito
mi_carrito = Carrito()

# Agregamos productos al carrito
mi_carrito.agregar_producto(producto1, 2)
mi_carrito.agregar_producto(producto2, 1)

# Mostramos los productos en el carrito
mi_carrito.ver_productos()

# Calculamos el total de compra
total_compra = mi_carrito.calcular_total()
print(f"Total de compra: ${total_compra}")

# Quitamos un producto del carrito
mi_carrito.quitar_producto(producto1)

# Mostramos los productos en el carrito
mi_carrito.ver_productos()

# Calculamos el total de compra actualizado
total_compra = mi_carrito.calcular_total()
print(f"Total de compra actualizado: ${total_compra}")
