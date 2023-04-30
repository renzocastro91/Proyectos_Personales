from Model import Task

class TaskController:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
    
    def complete_task(self, index):
        task = self.tasks[index]
        task.completed = True
    
    def delete_task(self, index):
        del self.tasks[index]
