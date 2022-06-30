#Funciones y Clases
from clases_agenda import * 
import funciones_agenda

#Programa

agenda = funciones_agenda.obtener_txt_como_objetos("contactos.txt")
print("-----------------------------------------------------------")
print("                  Bienvenidos a la Agenda!!!")
print("-----------------------------------------------------------")
while True:
    op = input("Que quieres hacer? \n 1- Buscar un contacto \n 2- Mostrar todos los contactos \n 3- Agregar un contacto \n 4- Eliminar un contacto \n 5- Modificar contacto \n 6 - Salir \n Ingrese:\t")
    if op == "1":
        x = funciones_agenda.buscar_contacto(agenda)
        if x == 0:
            funciones_agenda.contacto_inexistente()
    elif op == "2":
        funciones_agenda.mostrar_contactos(agenda)
    elif op == "3":
        funciones_agenda.agregar_contacto(agenda)
    elif op == "4":
        funciones_agenda.eliminar_contacto(agenda)
    elif op == "5":
        funciones_agenda.modificar_contacto(agenda)
    elif op == "6":
        break
    elif op == "7":
        #Opción de desarrollador, solo lo sabe el que programó
        funciones_agenda.reindexar_agenda(agenda)
    elif op == "8":
        funciones_agenda.mostrar_contacto2(agenda)

print("-----------------------------------------------------------")
print("        Gracias por utilizar la APP Mi Agenda!!!")
print("-----------------------------------------------------------")

funciones_agenda.cargar_lista_a_archivo("contactos.txt",agenda)


