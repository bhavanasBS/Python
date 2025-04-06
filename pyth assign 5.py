# Simple To-Do List Management System

# List to store tasks
tasks = []

# Function to display the menu
def show_menu():
    print("\nOptions:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

# Function to add a task
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

# Function to remove a task
def remove_task():
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks()
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"Task '{removed}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nPending Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Goodbye! Have a productive day.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
