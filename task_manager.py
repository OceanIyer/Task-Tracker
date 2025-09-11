import json
from datetime import datetime

try:
    with open("task.json", "r") as json_file:
        tasks = json.load(json_file)
        print(f"Current tasks:", [task['title'] for task in tasks])
except FileNotFoundError:
    tasks = []
    print("No existing task file found. A new one will be created.")

def add_task(tasks):
        raw_input = input("Enter task title: ")
        if raw_input == "back":
             return
        else:
             title = raw_input
        status = input("Enter task status (completed/pending): ")
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
def edit_task(tasks):
            for task in tasks:
                 print(f"ID: {task['id']}, {task['title']}")
            raw_input = input("Enter task ID to edit: ")
            if raw_input == 'back':
                 return
            else:
                 id = int(raw_input)
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
def help_menu(tasks):
        print("Available commands:")
        print("help - Show this help message")
        print("add - Add a new task")
        print("edit - Edit an existing task")
        print("delete - Delete a task")
        print("list - List all tasks")
        print("back - Return to main menu")
        print("exit - Exit the program")
def exit_program(tasks):
        print("Exiting the program.")
        exit()
def delete_task(tasks):
        print("Current tasks:", [f"ID: {task['id']}, Title: {task['title']}" for task in tasks])
        raw_input = input("Enter task ID to delete: ")
        if raw_input == "back":
             return
        else:
             id = int(raw_input)
        for task in tasks:
            if task['id'] == id:
                tasks.remove(task)
                with open("task.json", "w") as json_file:
                    json.dump(tasks, json_file, indent=4)
                    print("Task deleted successfully.")
                    break
        else:
            print("Task ID not found.")
def list_tasks(tasks): 
            if tasks == []:
                print("No tasks available.")
            else:
                type = input("Enter type of tasks to list (all/completed/pending/back): ").strip().lower()
                if type == 'back':
                     return
                elif type == "all":
                    for task in tasks:
                        print(f"ID: {task['id']}, Title: {task['title']}, Status: {task['status']}, Description: {task['description']}, Created At: {task['created_at']}")
                elif type == "completed":
                    for task in tasks:
                        if task['status'].lower() == 'completed':
                            print(f"ID: {task['id']}, Title: {task['title']}, Status: {task['status']}, Description: {task['description']}, Created At: {task['created_at']}")
                elif type == "pending":
                    for task in tasks:
                        if task['status'].lower() == 'pending':
                            print(f"ID: {task['id']}, Title: {task['title']}, Status: {task['status']}, Description: {task['description']}, Created At: {task['created_at']}")   
                else:
                    print("Invalid type. Please enter all, completed, or pending.")


command_dictionary = {
     "add": add_task,
     "edit": edit_task,
     "help": help_menu,
     "exit": exit_program,
     "delete": delete_task,
     "list": list_tasks
}

while True:
    command = input("Enter a command (help to list commands): ").strip().lower()
    
    if command in command_dictionary:
         command_dictionary[command](tasks)
    else:
         print("Invalid Command")