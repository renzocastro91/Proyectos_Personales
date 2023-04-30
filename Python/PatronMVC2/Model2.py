class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def edit_task(self, index, description):
        self.tasks[index].description = description

    def delete_task(self, index):
        del self.tasks[index]

    def mark_completed(self, index):
        self.tasks[index].completed = True

    def mark_pending(self, index):
        self.tasks[index].completed = False

    def get_task_list(self):
        return self.tasks