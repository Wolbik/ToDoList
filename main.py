from todo import ToDoList

# Función que muestra el menú de opciones al usuario
def menu():
    print("\n1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Editar tarea")
    print("4. Marcar tarea como completada")
    print("5. Eliminar tarea")
    print("6. Cerrar")

# Función principal que ejecuta el bucle del menú
def main():
    todo_list = ToDoList()  # Inicializa la lista de tareas

    while True:
        menu()  # Muestra el menú
        choice = input("Elige una opción: ")  # Espera la elección del usuario

        # Opción 1: Listar todas las tareas
        if choice == '1':
            todo_list.list_tasks()
        
        # Opción 2: Agregar una nueva tarea
        elif choice == '2':
            description = input("Descripción de la nueva tarea: ")
            todo_list.add_task(description)
        
        # Opción 3: Editar una tarea existente
        elif choice == '3':
            task_id = int(input("ID de la tarea a editar: "))
            new_description = input("Nueva descripción: ")
            if todo_list.edit_task(task_id, new_description):
                print("Tarea editada exitosamente.")
            else:
                print("ID de tarea no fue encontrado.")
        
        # Opción 4: Marcar una tarea como completada
        elif choice == '4':
            task_id = int(input("ID de la tarea a completar: "))
            if todo_list.complete_task(task_id):
                print("Tarea marcada como completada.")
            else:
                print("ID de tarea no encontrado.")
        
        # Opción 5: Eliminar una tarea
        elif choice == '5':
            task_id = int(input("ID de la tarea a eliminar: "))
            todo_list.delete_task(task_id)
            print("Tarea fue eliminada.")
        
        # Opción 6: Salir de la aplicación
        elif choice == '6':
            print("Saliendo de la aplicación...")
            break  # Sale del bucle y finaliza el programa
        
        # En caso de que el usuario elija una opción no válida
        else:
            print("Opción no válida.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
