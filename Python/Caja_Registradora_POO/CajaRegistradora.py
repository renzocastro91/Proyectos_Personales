from Clases_CR import * 
import Funciones_CR

#Programa
print("----------------------------------------------------------------------------")
print("               Bienvendos a la caja registradora N°XXXXX!!!")
print("----------------------------------------------------------------------------")

lista_articulos = Funciones_CR.obtener_txt_como_objetos("datos_articulos.txt",1)
lista_clientes = []

while True:
    print("----------------------------------------------------------------------------")
    op = input("Que quieres hacer? \n 1- Registrar una compra \n 2- Mostrar todos los artículos \n 3- Buscar un artículo \n 4- Agregar un artículo \n 5- Eliminar un artículo \n 6- Modificar Artículo \n 7 - Salir \n Ingrese:\t")
    if op == "1":
        Funciones_CR.registrar_compra(lista_articulos,lista_clientes)
    elif op == "2":
        Funciones_CR.mostrar_articulos(lista_articulos)
    elif op == "3":
        Funciones_CR.buscar_articulo(lista_articulos)
    elif op == "4":
        Funciones_CR.agregar_articulo(lista_articulos)
    elif op == "5":
        Funciones_CR.eliminar_articulo(lista_articulos)
    elif op == "6":
        Funciones_CR.modificar_articulo(lista_articulos)
    elif op == "7":
        break
    else:
        print("Opción ingresada incorrecta")
    print("----------------------------------------------------------------------------")
#Cargo lista de artículos modificados en el día al archivo principal
Funciones_CR.cargar_lista_a_archivo("datos_articulos.txt",lista_articulos,1)
print("----------------------------------------------------------------------------")
x = 0
for i in lista_clientes:
    x= x + i.monto_tot
print(f"Día Finalizado, total de clientes: {len(lista_clientes)} / Ingreso de dinero del día: ${x}")
print("----------------------------------------------------------------------------")

lista_registro_compra = Funciones_CR.obtener_txt_como_objetos("registro_compra.txt",2)
from datetime import datetime
fecha = datetime.today().strftime('%Y-%m-%d')
cod_nuevo = Funciones_CR.obtener_ultima_clave(lista_registro_compra) + 1
objeto_nuevo = Registro_compra(cod_nuevo,x,fecha)
lista_registro_compra.append(objeto_nuevo)
Funciones_CR.cargar_lista_a_archivo("registro_compra.txt",lista_registro_compra,2)