import pytest
from todo import ToDoList

# Usamos la función fixture de pytest para crear una lista de tareas temporal antes de cada test.
@pytest.fixture
def todo_list(tmpdir):
    # Se crea un archivo temporal "tasks.json" en un directorio temporal.
    file_path = tmpdir.join("tasks.json")
    # Se devuelve una instancia de la clase ToDoList con la ruta del archivo temporal.
    return ToDoList(file_path)

# Test para añadir una nueva tarea a la lista
def test_add_task(todo_list):
    # Se añade una nueva tarea a la lista.
    todo_list.add_task("Nueva tarea")
    # Se verifica que ahora haya una tarea en la lista.
    assert len(todo_list.tasks) == 1
    # Se verifica que la descripción de la primera tarea sea la esperada.
    assert todo_list.tasks[0]['description'] == "Nueva tarea"

# Test para editar una tarea existente en la lista
def test_edit_task(todo_list):
    # Se añade una tarea inicial.
    todo_list.add_task("Tarea vieja")
    # Se edita la primera tarea (id 1) cambiando su descripción.
    todo_list.edit_task(1, "Tarea nueva")
    # Se verifica que la descripción de la primera tarea haya cambiado correctamente.
    assert todo_list.tasks[0]['description'] == "Tarea nueva"

# Test para eliminar una tarea de la lista
def test_delete_task(todo_list):
    # Se añade una tarea que luego será eliminada.
    todo_list.add_task("Tarea a eliminar")
    # Se elimina la primera tarea (id 1).
    todo_list.delete_task(1)
    # Se verifica que no haya tareas en la lista tras la eliminación.
    assert len(todo_list.tasks) == 0

# Test para marcar una tarea como completada
def test_complete_task(todo_list):
    # Se añade una tarea que luego será marcada como completada.
    todo_list.add_task("Tarea a completar")
    # Se marca la primera tarea (id 1) como completada.
    todo_list.complete_task(1)
    # Se verifica que la tarea esté marcada como completada (True).
    assert todo_list.tasks[0]['completed'] == True
