from Controller import TaskController
from View import TaskView

class TaskApp:
    def __init__(self):
        self.controller = TaskController()
        self.view = TaskView(self.controller)
    
    def run(self):
        while True:
            self.view.show_tasks()
            print("1. Add task")
            print("2. Complete task")
            print("3. Delete task")
            print("4. Quit")
            
            choice = input("Enter choice: ")
            if choice == "1":
                self.view.add_task()
            elif choice == "2":
                self.view.complete_task()
            elif choice == "3":
                self.view.delete_task()
            elif choice == "4":
                break
            else:
                print("Invalid choice, please try again.")
        
        print("Goodbye!")
        
if __name__ == "__main__":
    app = TaskApp()
    app.run()
