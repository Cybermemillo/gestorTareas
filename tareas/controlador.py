from tareas.almacenamiento import loadTasks, saveTasks

def addTask(description, file):
    tasks = loadTasks(file)
    newID = max([task["id"] for task in tasks], default=0) + 1
    newTask = {
        "id": newID,
        "description": description,
        "completed": False
    }
    tasks.append(newTask)
    saveTasks(tasks, file)
    return f'Tarea añadida: {description}'

def showTasks(file):
    tasks = loadTasks(file)
    numberingTasks = ""
    for task in tasks:
        completed = "la tarea está completada." if task["completed"] else "la tarea no está completada."
        numberingTasks += f'{task["id"]}. {task["description"]}, {completed} \n'
    return numberingTasks