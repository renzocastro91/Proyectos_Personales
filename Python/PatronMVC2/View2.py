from Model2 import *

class ConsoleView:
    def __init__(self):
        pass

    def show_task_list(self, task_list):
        print("Tareas pendientes:")
        for i, task in enumerate(task_list):
            if not task.completed:
                print(f"{i+1}. {task.description}")
        print("\nTareas completadas:")
        for i, task in enumerate(task_list):
            if task.completed:
                print(f"{i+1}. {task.description}")
        print("")

    def add_task(self):
        description = input("Ingrese la descripción de la tarea: ")
        return Task(description)

    def edit_task(self):
        index = int(input("Ingrese el número de la tarea a editar: ")) - 1
        description = input("Ingrese la nueva descripción de la tarea: ")
        return index, description

    def delete_task(self):
        index = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
        return index

    def mark_completed(self):
        index = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1
        return index

    def mark_pending(self):
        index = int(input("Ingrese el número de la tarea a marcar como pendiente: ")) - 1
        return index