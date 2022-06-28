#Acá van a estar todas las funciones utilizadas en este programa
from Clases_CR import * 

def obtener_ultima_clave(lista):
	ultima_clave = lista[-1].codigo
	return ultima_clave

def obtener_txt_como_objetos(nombre_archivo,marca):
    if marca == 1:
        lista_articulos= []
        with open(nombre_archivo) as archivo:
            for linea in archivo:
                linea =linea.rstrip("\n")
                columnas = linea.split(",")
                cod = int(columnas[0])
                nom = columnas[1]
                marc = str(columnas[2])
                pre = float(columnas[3])
                sto = int(columnas[4])
                objeto = Articulo(cod,nom,marc,pre,sto)
                lista_articulos.append(objeto)
            return lista_articulos
    else:
        lista_registro= []
        with open(nombre_archivo) as archivo:
            for linea in archivo:
                linea =linea.rstrip("\n")
                columnas = linea.split(",")
                cod = int(columnas[0])
                monto_ac = float(columnas[1])
                fecha = str(columnas[2])
                objeto = Registro_compra(cod,monto_ac,fecha)
                lista_registro.append(objeto)
        return lista_registro

def cargar_lista_a_archivo(nombre_archivo,lista,marca):
    if marca == 1:
        with open(nombre_archivo, "w") as arch:
            for i in lista:
                x = i.devolver_atributos()
                arch.write(f"{x[0]},{x[1]},{x[2]},{x[3]},{x[4]}\n")
            arch.close()
        return arch
    else:
        with open(nombre_archivo, "w") as arch:
            for i in lista:
                x = i.devolver_atributos()
                arch.write(f"{x[0]},{x[1]},{x[2]}\n")
            arch.close()
        return arch

def registrar_compra(lista,listm):
    print("----------------------------------------------------------------------------")
    print("                             Registro de Compra")
    print("----------------------------------------------------------------------------")
    eleccion = input("Cómo desea hacer el registro? \n1- Manual (código de producto) \n2- Código de barra \nIngrese:\t")
    if eleccion == "1":
        c = 1
        monto = 0
        while True:
            cod = int(input("Ingrese el código de producto o 0 para finalizar el registro\t"))
            if cod == 0:
                break
            bandera = False
            for i in lista:
                if i.codigo == cod:
                    bandera = True
                    x = i
                    break
            if bandera:
                print("----------------------------------------------------------------------------")
                print(                                  f"Producto {c}")
                print("----------------------------------------------------------------------------")
                x.descripcion()
                print("----------------------------------------------------------------------------")
                cant = int(input("Ingrese la cantidad de unidades:\t"))
                x.cambiarstock(cant)
                monto = monto + x.precio
            else:
                print("----------------------------------------------------------------------------")
                print(                              "Producto no encontrado")
                print("----------------------------------------------------------------------------")
            c += 1
            print("----------------------------------------------------------------------------")
        objeto_carrito = Carrito(c,monto)
        listm.append(objeto_carrito)
        print("----------------------------------------------------------------------------")
        print(objeto_carrito.descripcion())
        print("----------------------------------------------------------------------------")
    elif eleccion == "2":
        c = 1
        monto = 0
        while True:
            print("Pase el producto por el código de barra \t")
            cod = emular_codigo_barra(lista)
            for i in lista:
                if i.codigo == cod:
                    print("----------------------------------------------------------------------------")
                    print(                                  f"Producto {c}")
                    print("----------------------------------------------------------------------------")
                    i.descripcion()
                    print("----------------------------------------------------------------------------")
                    cant = int(input("Ingrese la cantidad de unidades:\t"))
                    i.cambiarstock(cant)
                    monto = monto + i.precio
                    break
            c += 1
            op = input("Desea seguir pasando productos por el código de barra? s o n \nIngrese:\t")
            if op == "n":
                break
            print("----------------------------------------------------------------------------")
        listm.append(monto)
        print("----------------------------------------------------------------------------")
        print(                              f"Total a pagar: ${monto}")
        print("----------------------------------------------------------------------------")


def emular_codigo_barra(lista):
	import random
	ultima_clave = obtener_ultima_clave(lista)
	x = random.randint(1,ultima_clave)
	return x

def mostrar_articulos(lista):
    print("----------------------------------------------------------------------------")
    print("                             Lista de Artículos")
    print("----------------------------------------------------------------------------")
    for i in lista:
        i.descripcion()

def buscar_articulo(lista):
    print("----------------------------------------------------------------------------")
    print("                             Búsqueda de artículo")
    print("----------------------------------------------------------------------------")
    eleccion = input("Por qué quiere buscar? \n1- Por código de artículo \n2- Por nombre y marca \nIngrese:\t")
    if eleccion == "1":
        cod = int(input("Ingrese código del producto\t"))
        m1 = 0
        for i in lista:
            if i.codigo == cod:
                print("----------------------------------------------------------------------------")
                print("                             Producto Encontrado!")
                print("----------------------------------------------------------------------------")
                i.descripcion()
                m1 = 1
                break
        if m1 == 0:
            print("----------------------------------------------------------------------------")
            print("                            Producto no encotrado")
            print("----------------------------------------------------------------------------")
    elif eleccion == "2":
        nom = input("Ingrese nombre del producto\t")
        marc = input("Ingrese marca del producto\t")
        m1 = 0
        for i in lista:
            if i.nombre == nom and i.marca == marc:
                print("----------------------------------------------------------------------------")
                print("                             Producto Encontrado!")
                print("----------------------------------------------------------------------------")
                i.descripcion()
                m1 = 1
                break
        if m1 == 0:
            print("----------------------------------------------------------------------------")
            print("                            Producto no encotrado")
            print("----------------------------------------------------------------------------")

def agregar_articulo(lista):
    print("----------------------------------------------------------------------------")
    print("                            Agregar un artículo")
    print("----------------------------------------------------------------------------")
    cod = obtener_ultima_clave(lista) + 1
    nom = input("Ingrese nombre del producto\t")
    marc = input("Ingrese marca del producto\t")
    pre = float(input("Ingrese precio del producto\t"))
    sto = int(input("Ingrese el stock del producto\t"))
    objeto_nuevo = Articulo(cod,nom,marc,pre,sto)
    lista.append(objeto_nuevo)


def eliminar_articulo(lista):
    print("----------------------------------------------------------------------------")
    print("                            Eliminar un artículo")
    print("----------------------------------------------------------------------------")
    cod = int(input("Ingrese código de producto\t"))
    m1 = 0
    for i in lista:
        if i.codigo == cod:
            lista.remove(i)
            m1 = 1
            print("----------------------------------------------------------------------------")
            print("                             Producto Eliminado")
            print("----------------------------------------------------------------------------") 
    if m1 == 0:
        print("----------------------------------------------------------------------------")
        print("                             Produco no encontrado")
        print("----------------------------------------------------------------------------")

def modificar_articulo(lista):
    print("----------------------------------------------------------------------------")
    print("                            Modificar un artículo")
    print("----------------------------------------------------------------------------")
    cod = int(input("Ingrese código del producto que desea modificar\t"))
    m1 = 0
    for i in lista:
        if i.codigo == cod:
            m1 = 1
            op = input("Que desea cambiar? \n 1- Nombre \n 2- Marca \n 3- Precio \n 4- Stock \n 5- Nada \n Ingrese:\t")
            if op == "1":
                nom = input("Ingrese nuevo nombre de artículo:\t")
                i.modificar_nombre(nom)
            elif op == "2":
                marc = input("Ingrese nueva marca de producto:\t")
                i.modificar_marca(marc)
            elif op == "3":
                pre = float(input("Ingrese nuevo precio:\t"))
                i.modificar_precio(pre)
            elif op == "4":
                sto = int(input("Ingrese nuevo stock:\t"))
                i.modificar_stock(sto)
            elif op == "5":
                break
            print("----------------------------------------------------------------------------")
            print("                            Producto Modificado")
            print("----------------------------------------------------------------------------")   
    if m1 == 0:
        print("----------------------------------------------------------------------------")
        print("                            Producto No encontrado")
        print("----------------------------------------------------------------------------")
        
    