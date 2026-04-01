import json

tasks = []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)


def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    except json.JSONDecodeError:
        print("Warning: tasks.json is invalid. Starting with empty task list.")
        tasks = []


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
        status = "Done" if task.get("completed") else "Pending"
        deadline = task.get("deadline", "N/A")
        print(f"{i+1}. {task['title']} | {task['priority']} | {deadline} | {status}")
    print()


def mark_complete():
    if not tasks:
        print("No tasks to mark complete.\n")
        return

    view_tasks()
    try:
        num = int(input("Enter task number to mark complete: "))
    except ValueError:
        print("Invalid number.\n")
        return

    if 0 < num <= len(tasks):
        tasks[num-1]["completed"] = True
        save_tasks()
        print("Task marked as complete!\n")
    else:
        print("Invalid task number\n")


def delete_task():
    if not tasks:
        print("No tasks to delete.\n")
        return

    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
    except ValueError:
        print("Invalid number.\n")
        return

    if 0 < num <= len(tasks):
        tasks.pop(num-1)
        save_tasks()
        print("Task deleted!\n")
    else:
        print("Invalid task number\n")


def sort_tasks():
    if not tasks:
        print("No tasks to sort.\n")
        return

    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    tasks.sort(key=lambda x: priority_order.get(x.get("priority", ""), 4))
    save_tasks()
    print("Tasks sorted by priority!\n")


def main():
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. Sort Tasks by Priority")
        print("6. Exit")

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
            sort_tasks()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice\n")


if __name__ == "__main__":
    load_tasks()
    main()

