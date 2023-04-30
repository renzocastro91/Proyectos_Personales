from Model2 import *
from View2 import *

class TaskController:
    def __init__(self):
        self.task_list = TaskList()
        self.view = ConsoleView()

    def run(self):
        while True:
            self.view.show_task_list(self.task_list.get_task_list())
            print("¿Qué acción desea realizar?")
            print("1. Agregar tarea")
            print("2. Editar tarea")
            print("3. Eliminar tarea")
            print("4. Marcar tarea como completada")
            print("5. Marcar tarea como pendiente")
            print("6. Salir")
            choice = int(input("> "))
            if choice == 1:
                task = self.view.add_task()
                self.task_list.add_task(task)
            elif choice == 2:
                index, description = self.view.edit_task()
                self.task_list.edit_task(index, description)
            elif choice == 3:
                index = self.view.delete_task()
                self.task_list.delete_task(index)
            elif choice == 4:
                index = self.view.mark_completed()
                self.task_list.mark_completed(index)
            elif choice == 5:
                index = self.view.mark_pending()
                self.task_list.mark_pending(index)
            elif choice == 6:
                break
            else:
                print("Opción no válida.")


if __name__ == '__main__':
    controller = TaskController()
    controller.run()