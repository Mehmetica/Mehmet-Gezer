
from task_management import TaskManagement
from datetime import datetime

class TaskEditing:
    def __init__(self, task_management):
        self.task_management = task_management

    def set_task_status(self, task_id, status):
        try:
            task = self.task_management.get_task_by_id(task_id)
            task.status = status
            print(f"Task '{task_id}' status updated to '{status}'.")
        except IndexError:
            print("Error: Invalid task index.")
        
    
    def set_prioritization(self, task_id, priority):
        try:
            task = self.task_management.get_task_by_id(task_id)
            task.priority = priority
            print(f"Task '{task.title}' priority updated to '{priority}'.")
        except IndexError:
            print("Error: Invalid task index.")

        
    
    def set_new_date(self, task_id, deadline):
        try:
            task = self.task_management.get_task_by_id(task_id)
            task.deadline = datetime.strptime(deadline, "%Y-%m-%d")
            print(f"Task {task_id} deadline updated to {deadline}")
        except IndexError:
            print("Error: Invalid task index.")
        
    
    def mark_status_completed(self, task_id):
        task = self.task_management.get_task_by_id(task_id)
        if task:
            task.status = "Completed"
            print(f"Task {task_id} marked as completed")
    
    def get_task_by_id(self, task_id):
        for task in self.task_management.task_list:
            if task.task_id == task_id:
                return task
        return None
