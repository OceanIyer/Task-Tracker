import json
from datetime import datetime

try:
    with open("task.json", "r") as json_file:
        tasks = json.load(json_file)
        print(f"Current tasks:", [task['title'] for task in tasks])
except FileNotFoundError:
    tasks = []
    print("No existing task file found. A new one will be created.")


while True:
    command = input("Enter a command (help to list commands): ").strip().lower()

    if command == "help":
        print("Available commands:")
        print("help - Show this help message")
        print("add - Add a new task")
        print("edit - Edit an existing task")
        print("delete - Delete a task")
        print("list - List all tasks")
        print("exit - Exit the program")
    elif command == "exit":
        print("Exiting the program.")
        exit()
    elif command == "add":
        title = input("Enter task title: ")
        status = input("Enter task status: ")
        description = input("Enter task description: ")

        if len(tasks) == 0:
            new_id = 1
        else:
            new_id = tasks[-1]['id'] + 1


        new_task = {
            "id": new_id,
            "title": title,
            "status": status,
            "description": description,
            "created_at": datetime.now().isoformat()
        }

        tasks.append(new_task)

        with open("task.json", "w") as json_file:
            json.dump(tasks, json_file, indent=4)
            print("Task added successfully.")
    elif command == "edit":
            id = int(input("Enter task ID to edit: "))
            if not any(task['id'] == id for task in tasks):
                print("Task ID not found.")
            else:
                for task in tasks:
                        if task['id'] == id:
                            edit = input("What would you like to edit? (title/status/description): ").strip().lower()
                            if edit == 'title':
                                new_title = input("Enter new title: ")
                                task['title'] = new_title
                            elif edit == 'status':
                                new_status = input("Enter new status: ")
                                task['status'] = new_status
                            elif edit == 'description':
                                new_description = input("Enter new description: ")
                                task['description'] = new_description
                            else:
                                print("Invalid edit option.")

                            with open("task.json", "w") as json_file:
                                json.dump(tasks, json_file, indent=4)
                                print("Task updated successfully.")
                            break
    elif command == "delete":
        print("Current tasks:", [f"ID: {task['id']}, Title: {task['title']}" for task in tasks])
        id = int(input("Enter task ID to delete: "))
        for task in tasks:
            if task['id'] == id:
                tasks.remove(task)
                with open("task.json", "w") as json_file:
                    json.dump(tasks, json_file, indent=4)
                    print("Task deleted successfully.")
                    break
        else:
            print("Task ID not found.")

    elif command == "list":
        if tasks == []:
            print("No tasks available.")
        else:
            for task in tasks:
                print(f"ID: {task['id']}, Title: {task['title']}, Status: {task['status']}, Description: {task['description']}, Created At: {task['created_at']}")