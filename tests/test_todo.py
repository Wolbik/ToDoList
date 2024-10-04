import pytest
from todo import ToDoList

@pytest.fixture
def todo_list(tmpdir):
    file_path = tmpdir.join("tasks.json")
    return ToDoList(file_path)

def test_add_task(todo_list):
    todo_list.add_task("Nueva tarea")
    assert len(todo_list.tasks) == 1
    assert todo_list.tasks[0]['description'] == "Nueva tarea"

def test_edit_task(todo_list):
    todo_list.add_task("Tarea vieja")
    todo_list.edit_task(1, "Tarea nueva")
    assert todo_list.tasks[0]['description'] == "Tarea nueva"

def test_delete_task(todo_list):
    todo_list.add_task("Tarea a eliminar")
    todo_list.delete_task(1)
    assert len(todo_list.tasks) == 0

def test_complete_task(todo_list):
    todo_list.add_task("Tarea a completar")
    todo_list.complete_task(1)
    assert todo_list.tasks[0]['completed'] == True
