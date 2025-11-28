
from flask import Flask, render_template, request, redirect
import json
import os
from dotenv import load_dotenv
from backend.task_handler import (
    load_tasks,
    save_tasks,
    add_task,
    update_task_status,
    update_task_description,
    delete_task
)



load_dotenv()
app = Flask(__name__)
appMain = os.environ.get('appMain')

# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    tasks = load_tasks()
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["status"] == "Completed")
    pending_tasks = total_tasks - completed_tasks
    progress_percentage = int((completed_tasks / total_tasks * 100)) if total_tasks > 0 else 0
    
    return render_template(
        "index.html",
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks,
        progress_percentage=progress_percentage,
        appMain=appMain
    )


# ---------------- ADD TASK ----------------
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["description"]
        add_task(title, desc)
        return redirect("/tasks")
    return render_template("add.html", appMain=appMain)


# ---------------- VIEW TASKS ----------------
@app.route("/tasks")
def tasks():
    tasks = load_tasks()
    return render_template("tasks.html", tasks=tasks, appMain=appMain)


# ---------------- UPDATE TASK ----------------
@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        task_id = int(request.form["task_id"])
        new_desc = request.form.get("description")
        completed = request.form.get("completed")

        msg = ""
        if new_desc:
            msg = update_task_description(task_id, new_desc)
        if completed:
            msg = update_task_status(task_id)

        return render_template("update.html", message=msg, appMain=appMain)

    return render_template("update.html",tasks=load_tasks(), appMain=appMain)


# ---------------- DELETE TASK ----------------
@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        task_id = int(request.form["task_id"])
        msg = delete_task(task_id)
        return render_template("delete.html", message=msg, appMain=appMain)

    return render_template("delete.html", appMain=appMain)


if __name__ == "__main__":
    app.run(debug=True)
