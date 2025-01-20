import json

def loadTasks(file: str) -> list:
    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def saveTasks(taskList: list, file: str):
    with open(file, "w") as f:
        json.dump(taskList, f, indent=4)