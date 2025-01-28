
from task_management import TaskManagement
from task_editing import TaskEditing
from task_tracking import TaskTracking
from task_scheduling import TaskScheduling

# Create a Task Management instance
t1 = TaskManagement()

# Initialize Task Editing and Task Tracking
te = TaskEditing(t1)
tt = TaskTracking(t1)

# TaskScheduling ile task oluştur
ts = TaskScheduling(t1)

# Create and add tasks to the task list
ts.create_personal_task(1, "P1", "today")
ts.create_work_task(2, "W2", "next week")

# Display tasks
print("Displaying tasks after creation:")
t1.display_tasks()

# Set the status of Task 1 to "In Progress"
te.set_task_status(1, "In Progress")

# Mark Task 1 as completed
te.mark_status_completed(1)

# Set the priority of Task 1 to 'Not Important'
te.set_prioritization(1, "Not Important")

# Get Task 2's color
print(f"Task with ID 2's color is {tt.get_task_color(2)}.")

# Display tasks again after updates
print("Displaying tasks after updates:")
t1.display_tasks()
