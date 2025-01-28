
from datetime import datetime

class TaskManagement:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def display_tasks(self):
        if not self.task_list:
            print("No tasks to display.")
        for task in self.task_list:
            print(task)

