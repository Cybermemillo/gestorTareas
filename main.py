from tareas.controlador import addTask, showTasks, completeTask, deleteTask
import os as os

def main():
    file_path = "./gestorPython/json/tareas.json"
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            file.write('[]')  # Inicializar con una lista vacía
            
    opcion: int = None
    while opcion != 0:
        try:
            print("Gestor de tareas \n 1. Mostrar tareas \n 2. Añadir tarea \n 3. Completar tarea \n 4. Borrar tarea \n 0. Salir \n")
            opcion = int(input("Introduce una opción: "))
            if opcion >= 0 and opcion <= 4:
                match opcion:
                    case 1:
                        print("\nHas seleccionado ver las tareas.\n")
                        print(showTasks(file_path))
                    case 2:
                        print("\nHas seleccionado añadir tarea.\n")
                        descripcion = input("Introduce la descripción de la tarea: ")
                        addTask(descripcion, file_path)
                        print("Se ha añadido la tarea.")
                    case 3:
                        print("\nHas seleccionado marcar como completada una tarea\n")
                        task_id = int(input("Introduce el número de la tarea que quieres completar: "))
                        completeTask(task_id, file_path)
                    case 4:
                        print("Has seleccionado borrar una tarea \n")
                        task_id = int(input("Introduce el número de la tarea a borrar: "))
                        deleteTask(task_id, file_path)
                    case 0:
                        return None
                    case _:
                        print("Introduce una opción correcta.")
            else:
                print("Introduce una opción correcta.")
        except ValueError:
            print("Por favor, introduce un número válido.")
        except KeyboardInterrupt:
            print("\nSaliendo del gestor de tareas. Ten un buen día.")
            break

if __name__ == "__main__":
    main()