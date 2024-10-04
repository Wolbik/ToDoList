import json
import os

# todo.py (modificación intencionada para provocar fallos)
class ToDoList:
    def __init__(self, file_path='data/tasks.json'):
        self.file_path = file_path
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description):
        task = {'id': len(self.tasks) + 1, 'description': description, 'completed': False}
        self.tasks.append(task)
        self.save_tasks()

    def edit_task(self, task_id, new_description):
        for task in self.tasks:
            if task['id'] == task_id:
                task['description'] = new_description
                self.save_tasks()
                return True
        return False

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        self.save_tasks()

    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                return True
        return False

    def list_tasks(self):
        if not self.tasks:
            print("No tienes tareas pendientes.")
        for task in self.tasks:
            status = "Completada" if task['completed'] else "Pendiente"
            print(f"ID: {task['id']} - {task['description']} [{status}]")
