import json
import os

TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")

tasks = []


def load_tasks():
    global tasks
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r", encoding="utf-8") as f:
                tasks = json.load(f)
        except (json.JSONDecodeError, IOError):
            print("Warning: couldn't load tasks.json. Starting with an empty task list.")
            tasks = []
    else:
        tasks = []


def save_tasks():
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2)
    except IOError:
        print("Error: unable to save tasks to tasks.json.")


def add_task():
    title = input("Enter task title: ")
    priority = input("Enter priority (High/Medium/Low): ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")

    task = {
        "title": title,
        "priority": priority,
        "deadline": deadline,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!\n")

def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return

    for i, task in enumerate(tasks):
        status = "Done" if task.get("completed") else "Pending"
        print(f"{i+1}. {task['title']} | {task['priority']} | {task['deadline']} | {status}")
    print()


def mark_complete():
    view_tasks()
    num = int(input("Enter task number to mark complete: "))
    
    if 0 < num <= len(tasks):
        tasks[num-1]["completed"] = True
        print("Task marked as complete!\n")
    else:
        print("Invalid task number\n")


def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: "))
    
    if 0 < num <= len(tasks):
        tasks.pop(num-1)
        print("Task deleted!\n")
    else:
        print("Invalid task number\n")


def main():
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()