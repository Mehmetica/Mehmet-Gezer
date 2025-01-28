
from abc import ABC, abstractmethod
from datetime import datetime

class Task(ABC):
    def __init__(self, task_id, task_name, deadline):
        self.task_id = task_id
        self.task_name = task_name
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.status = "Pending"
        self.priority = "Low"
        self.color = "Blue"

    @abstractmethod
    def color_your_task(self):
        pass

    def days_to_accomplish_task(self):
        return (self.deadline - datetime.now()).days

    def __str__(self):
        return f"Task ID: {self.task_id}, Name: {self.task_name}, Deadline: {self.deadline.strftime('%Y-%m-%d')}, Color: {self.color}, Status: {self.status}, Priority: {self.priority}, Remaining Days: {self.days_to_accomplish_task()}"

