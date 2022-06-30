#Acá van todas las funciones utilizadas en el programa

from clases_agenda import *

def contacto_inexistente():
    print("-----------------------------------------------------------")
    print("                  Contacto inexsistente")
    print("-----------------------------------------------------------")

def obtener_ultima_clave(lista):
	ultima_clave = lista[-1].codigo
	return ultima_clave

def obtener_txt_como_objetos(nombre_archivo):
    lista_contactos= []
    with open(nombre_archivo) as archivo:
        for linea in archivo:
            linea =linea.rstrip("\n")
            columnas = linea.split(",")
            cod = int(columnas[0])
            nom = columnas[1]
            tel1 = int(columnas[2])
            tel2 = int(columnas[3])
            dire = str(columnas[4])
            objeto = Contacto(cod,nom,tel1,tel2,dire)
            lista_contactos.append(objeto)
        return lista_contactos


def cargar_lista_a_archivo(nombre_archivo,lista):
    with open(nombre_archivo, "w") as arch:
        for i in lista:
            x = i.devolver_atributos()
            arch.write(f"{x[0]},{x[1]},{x[2]},{x[3]},{x[4]}\n")
        arch.close()
    return arch

def buscar_contacto(lista):
    print("-----------------------------------------------------------")
    print("                  Búsqueda de contacto!!!")
    print("-----------------------------------------------------------")
    nom = input("Ingrese nombre del contacto:\t")
    for i in lista:
        if i.nombre == nom:
            print("-----------------------------------------------------------")
            print("                  Contacto Encontrado!!!")
            print("-----------------------------------------------------------")
            print(i.descripcion())
            return i    
    return 0

def mostrar_contactos(lista):
    print("-----------------------------------------------------------------------------")
    print("                                  Contactos")
    print("------------------------------------------------------------------------------")
    for i in lista:
        print(i.descripcion())
        print("---------------------------------------------------------------------------")

def agregar_contacto(lista):
    print("-----------------------------------------------------------")
    print("                     Agregar contacto!")
    print("-----------------------------------------------------------")
    while True:
        cod = obtener_ultima_clave(lista) + 1
        nom = input("Ingrese nombre de contacto:\t")
        tel1 = int(input("Ingrese Teléfono 1:\t"))
        op = input("Desea agregar un segundo teléfono? s o n\t")
        if op.lower() == "s":
            tel2 = int(input("Ingrese el segundo teléfono:\t"))
        else:
            tel2 = 0 
        dire = input("Ingrese la dirección:\t")
        objeto_nuevo  = Contacto(cod,nom,tel1,tel2,dire)
        lista.append(objeto_nuevo)
        print("-----------------------------------------------------------")
        op = input("Desea cargar otro contacto? s o n\t")
        if op == "n":
            break

def eliminar_contacto(lista):
    print("-----------------------------------------------------------")
    print("                    Eliminar un contacto")
    print("-----------------------------------------------------------")
    x = buscar_contacto(lista)
    if x != 0:
        lista.remove(x)
        print("-----------------------------------------------------------")
        print("                     Contacto Eliminado")
        print("-----------------------------------------------------------")
    else:
        contacto_inexistente()

def modificar_contacto(lista):
    op = input("Que desea modificar? \n 1- Nombre \n 2- Teléfono 1 \n 3- Teléfono 2 \n 4-Dirección \5 Nada \n Ingrese:\t")
    m1 = 0
    if op == "1":
        x = buscar_contacto(lista)
        if x != 0:
            nom = input("Ingrese nuevo nombre de contacto:\t")
            x.cambiar_nombre(nom)
        else:
            contacto_inexistente()
        m1 = 1
    elif op == "2":
        x = buscar_contacto(lista)
        if x != 0:
            tel1 = int(input("Ingrese nuevo número de teléfono:\t"))
            x.cambiar_telefono1(tel1)
        else:
            contacto_inexistente()
        m1 = 1
    elif op == "3":
        x = buscar_contacto(lista)
        if x != 0:
            tel2 = int(input("Ingrese nuevo número de teléfono\t"))
            x.cambiar_telefono2(tel2)
        else:
            contacto_inexistente()
        m1 = 1
    elif op == "4":
        x = buscar_contacto(lista)
        if x != 0:
            dire = input("Ingrese nueva dirección:\t")
            x.cambiar_direccion(dire)
        else:
            contacto_inexistente()
        m1 = 1
    if m1 == 0:
        print("-----------------------------------------------------------")
        print("    No se ha modificado ningún atributo del contacto")
        print("-----------------------------------------------------------")
    else:
        print("-----------------------------------------------------------")
        print("                  Contacto modificado!!")
        print("-----------------------------------------------------------")

def reindexar_agenda(lista):
    c = 1
    for i in lista:
        i.cambiar_codigo(c)
        c += 1
    
def mostrar_contacto2(lista):
    for i in lista:
        print(i.descripcion_dev())