from todo import ToDoList

def menu():
    print("\n1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Editar tarea")
    print("4. Marcar tarea como completada")
    print("5. Eliminar tarea")
    print("6. Salir")

def main():
    todo_list = ToDoList()

    while True:
        menu()
        choice = input("Elige una opción: ")

        if choice == '1':
            todo_list.list_tasks()
        elif choice == '2':
            description = input("Descripción de la nueva tarea: ")
            todo_list.add_task(description)
        elif choice == '3':
            task_id = int(input("ID de la tarea a editar: "))
            new_description = input("Nueva descripción: ")
            if todo_list.edit_task(task_id, new_description):
                print("Tarea editada exitosamente.")
            else:
                print("ID de tarea no fue encontrado.")
        elif choice == '4':
            task_id = int(input("ID de la tarea a completar: "))
            if todo_list.complete_task(task_id):
                print("Tarea marcada como completada.")
            else:
                print("ID de tarea no encontrado.")
        elif choice == '5':
            task_id = int(input("ID de la tarea a eliminar: "))
            todo_list.delete_task(task_id)
            print("Tarea eliminada.")
        elif choice == '6':
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
