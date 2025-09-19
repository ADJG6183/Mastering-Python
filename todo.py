todos = []

def save_tasks(todos):
    with open("tasks.txt", "w") as file:
        for item in todos:
            file.write(f"{item}\n")
    print("Tasks saved to tasks.txt")

def add_todo(item):
    todos.append(item)
    print(f'Added todo: "{item}"') 
    save_tasks(todos)

def list_todos():
    if not todos:
        print("No tasks found. Please add tasks.")
    else:
        for idx, item in enumerate(todos, start=1):
            print(f"{idx}. {item}")


def remove_todo(index):
    if 0 <= index < len(todos):
        removed = todos.pop(index)
        print(f"Removed the selected task: '{removed}'")
    else:
        print("Invalid task number.")
        save_tasks(todos)

def clear_todos():
    todos.clear()
    print("All tasks cleared.")

if __name__ == "__main__":
    print (""""
    1.Add Task
    2.Delete a Task
    3.List the tasks
    4.Remove all tasks
    5.Quit
    """)
    ans = input("What would you like to do?")
    if ans=="1":
        task = input("Enter the task: ")
        add_todo(task)
    elif ans=="2":
        index = int(input("Enter the task number to delete: ")) - 1
        remove_todo(index)
    elif ans=="3":
        list_todos()
    elif ans=="4":
        clear_todos()
    elif ans=="5":
        print("\n Goodbye")
        ans = False 
    elif ans !="":
        print("\n Not Valid Choice Try again") 