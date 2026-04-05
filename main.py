import json
import os

TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")

tasks = []

def load_tasks():
    global tasks
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as f:
                tasks = json.load(f)
        except:
            tasks = []
    else:
        tasks = []


def save_tasks():
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


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
    save_tasks()
    print("Task added successfully!\n")


def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return

    for i, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Pending"
        print(f"{i+1}. {task['title']} | {task['priority']} | {task['deadline']} | {status}")
    print()


def mark_complete():
    view_tasks()
    num = int(input("Enter task number to mark complete: "))
    
    if 0 < num <= len(tasks):
        tasks[num-1]["completed"] = True
        save_tasks()
        print("Task marked as complete!\n")
    else:
        print("Invalid task number\n")


def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: "))
    
    if 0 < num <= len(tasks):
        tasks.pop(num-1)
        save_tasks()
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
    load_tasks()
    main()