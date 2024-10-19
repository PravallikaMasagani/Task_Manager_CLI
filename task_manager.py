import json
import os


# Class to represent a Task with an ID, title, and completion status
class Task:
    def __init__(self, task_id, title):
        self.id = task_id
        self.title = title
        self.completed = False

    # Convert the task into a dictionary (for saving to file)
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }

    # Create a task from a dictionary (for loading from file)
    def from_dict(data):
        task = Task(data['id'], data['title'])
        task.completed = data['completed']
        return task


# Class to manage tasks and handle file operations
class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.tasks = []  # List to store tasks
        self.filename = filename
        self.load_tasks()  # Load tasks from file at startup

    # Add a new task to the task list
    def add_task(self, title):
        task_id = len(self.tasks) + 1
        task = Task(task_id, title)
        self.tasks.append(task)
        self.save_tasks()  # Save tasks to file

    # Display all tasks with their status (completed or not)
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            status = "Completed" if task.completed else "In completed"
            print(f"{task.id}: {task.title} [{status}]")

    # Delete a task by its ID
    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()  # Save changes to file

    # Mark a task as complete by its ID
    def mark_task_complete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                self.save_tasks()  # Save updated status to file
                return
        print("Task not found.")

    # Save the task list to a JSON file
    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file)

    # Load tasks from the JSON file into the task list
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task.from_dict(data) for data in tasks_data]


# Function to handle user login
def login():
    correct_email = "user@example.com"
    correct_password = "password123"

    # Prompt user for email and password
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check credentials
    if email == correct_email and password == correct_password:
        print("Login successful!")
    else:
        print("Invalid email or password. Exiting...")
        exit()


# Main function to run the CLI menu and handle user input
def main():
    manager = TaskManager()  # Create TaskManager instance

    print("Welcome to the Task Manager CLI!")
    while True:
        # Display the menu options
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Exit")

        # Get the user's choice
        choice = input("Choose an option: ")

        # Handle each menu option
        if choice == '1':
            title = input("Enter task title: ")
            manager.add_task(title)
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark as complete: "))
            manager.mark_task_complete(task_id)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")


# Run the login and main functions when the script is executed
if __name__ == "__main__":
    login()
    main()
