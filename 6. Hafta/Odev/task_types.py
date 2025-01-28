
from task import Task

class PersonalTask(Task):
    def __init__(self, task_id, task_name, deadline):
        super().__init__(task_id, task_name, deadline)
        self.priority = "Low"
        self.color = "Blue"

    def color_your_task(self):
        self.color = "Blue"

class WorkTask(Task):
    def __init__(self, task_id, task_name, deadline):
        super().__init__(task_id, task_name, deadline)
        self.priority = "High"
        self.color = "Red"

    def color_your_task(self):
        self.color = "Red"
