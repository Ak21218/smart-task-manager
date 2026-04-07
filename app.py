from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


@app.route("/", methods=["GET", "POST"])
def home():
    tasks = load_tasks()

    if request.method == "POST":
        title = request.form["title"]
        priority = request.form["priority"]
        deadline = request.form["deadline"]

        tasks.append({
            "title": title,
            "priority": priority,
            "deadline": deadline,
            "completed": False
        })

        save_tasks(tasks)
        return redirect("/")

    return render_template("index.html", tasks=tasks)


@app.route("/complete/<int:index>")
def complete_task(index):
    tasks = load_tasks()
    tasks[index]["completed"] = True
    save_tasks(tasks)
    return redirect("/")


@app.route("/delete/<int:index>")
def delete_task(index):
    tasks = load_tasks()
    tasks.pop(index)
    save_tasks(tasks)
    return redirect("/")


app.run(debug=True)