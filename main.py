tasks = []




def add_task():
    title = input("Enter task title: ")
    priority = input("Enter priority (High/Medium/Low): ")

    task = {
        "title": title,
        "priority": priority,
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
        print(f"{i+1}. {task['title']} | {task['priority']} | {status}")
    print()





def main():
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice\n")


if __name__ == "__main__":
    main()

