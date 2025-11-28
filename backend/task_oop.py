class Task:
    def __init__(self, task_id, title, description, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def mark_completed(self):
        self.status = "Completed"

    def update_description(self, new_desc):
        self.description = new_desc

    def display_task_info(self):
        print(f"ID: {self.task_id}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")


# Demonstration
if __name__ == "__main__":
    t1 = Task(1, "Study", "Finish Python assignment")
    t2 = Task(2, "Exercise", "Go for a run")

    t1.update_description("Finish Flask assignment")
    t2.mark_completed()

    t1.display_task_info()
    print()
    t2.display_task_info()
