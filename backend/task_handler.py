import json
import os

FILE = "tasks.json"


def load_tasks():
    try:
        if not os.path.exists(FILE):
            with open(FILE, "w") as f:
                json.dump([], f)

        with open(FILE, "r") as f:
            return json.load(f)

    except json.JSONDecodeError:
        return []



def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)



def add_task(title, description):
    tasks = load_tasks()
    task_id = len(tasks) + 1

    new_task = {
        "task_id": task_id,
        "title": title,
        "description": description,
        "status": "Pending"
    }

    tasks.append(new_task)
    save_tasks(tasks)



def update_task_description(task_id, new_desc):
    tasks = load_tasks()
    for task in tasks:
        if task["task_id"] == task_id:
            task["description"] = new_desc
            save_tasks(tasks)
            return "Description updated successfully"
    return "Task not found"

 
def update_task_status(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["task_id"] == task_id:
            task["status"] = "Completed"
            save_tasks(tasks)
            return "Task marked as completed"
    return "Task not found"


 
def delete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["task_id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return "Task deleted successfully"
    return "Task not found"
