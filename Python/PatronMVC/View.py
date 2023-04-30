class TaskView:
    def __init__(self, controller):
        self.controller = controller
    
    def show_tasks(self):
        print("TASKS:")
        for i, task in enumerate(self.controller.tasks):
            status = "COMPLETED" if task.completed else "INCOMPLETE"
            print(f"{i+1}. {task.description} - {status}")
    
    def add_task(self):
        description = input("Enter task description: ")
        self.controller.add_task(description)
        print("Task added successfully!")
    
    def complete_task(self):
        index = int(input("Enter task number to complete: ")) - 1
        self.controller.complete_task(index)
        print("Task completed!")
    
    def delete_task(self):
        index = int(input("Enter task number to delete: ")) - 1
        self.controller.delete_task(index)
        print("Task deleted!")
