import json

def loadTasks(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def saveTasks(taskList, file):
    with open(file, "w") as f:
        json.dump(taskList, f, indent=4)