
from task_types import PersonalTask, WorkTask
from task_management import TaskManagement
from datetime import datetime, timedelta

SPECIAL_KEYWORDS = {
    "today": datetime.now().strftime("%Y-%m-%d"),
    "tomorrow": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
    "next week": (datetime.now() + timedelta(weeks=1)).strftime("%Y-%m-%d")
}

class TaskScheduling:
    def __init__(self, task_management):
        self.task_management = task_management

    def create_personal_task(self, task_id, task_name, deadline):
        if deadline in SPECIAL_KEYWORDS:
            deadline = SPECIAL_KEYWORDS[deadline]
        task = PersonalTask(task_id, task_name, deadline)
        self.task_management.add_task(task)

    def create_work_task(self, task_id, task_name, deadline):
        if deadline in SPECIAL_KEYWORDS:
            deadline = SPECIAL_KEYWORDS[deadline]
        task = WorkTask(task_id, task_name, deadline)
        self.task_management.add_task(task)
