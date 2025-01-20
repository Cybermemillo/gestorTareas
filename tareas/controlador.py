from tareas.almacenamiento import loadTasks, saveTasks

def addTask(description: str, file: str) -> str:
    tasks: list = loadTasks(file)
    newID: int = max([task["id"] for task in tasks], default=0) + 1
    newTask = {
        "id": newID,
        "description": description,
        "completed": False
    }
    tasks.append(newTask)
    saveTasks(tasks, file)
    return f'Tarea añadida: {description}'

def showTasks(file: str) -> str:
    tasks = loadTasks(file)
    numberingTasks = ""
    for task in tasks:
        completed = "la tarea está completada." if task["completed"] else "la tarea no está completada."
        numberingTasks += f'{task["id"]}. {task["description"]}, {completed} \n'
    return numberingTasks

def completeTask(task_id: int, file: str) -> bool:
    tasks = loadTasks(file)
    for task in tasks:
        if task["id"] == int(task_id):
            task["completed"] = True
            saveTasks(tasks, file)
            return True
    return False

def deleteTask(task_id, file):
        tasks = loadTasks(file)
        tasks = [task for task in tasks if task["id"] != task_id]
        for index, task in enumerate(tasks, start=1):
            task["id"] = index
        saveTasks(tasks, file)
        print(f"Tarea con número {task_id} eliminada.")