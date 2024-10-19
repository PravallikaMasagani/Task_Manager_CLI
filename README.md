# Task Manager CLI Application

## Project Description
This is a simple command-line interface (CLI) Task Manager application written in Python. It allows users to manage tasks by adding, viewing, deleting, and marking them as completed. The tasks are saved to and loaded from a JSON file, so they persist between runs of the program. The user must log in with a predefined email and password to access the application.

## Features
- **Add Task:** Allows the user to add new tasks.
- **View Tasks:** Displays all tasks along with their completion status.
- **Delete Task:** Removes a task by its ID.
- **Mark Task as Complete:** Marks a specific task as completed.
- **File Persistence:** Tasks are saved to a `tasks.json` file and loaded on program start.

## Login Credentials
To access the task manager, the user must log in with the following credentials:
- **Email:** `user@example.com`
- **Password:** `password123`

## How to Run the Application
### Requirements:
- Python 3.x installed on your machine.

### Steps to run:
1. Clone or download this repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the following command to start the Task Manager:
   ```bash
   python task_manager.py
