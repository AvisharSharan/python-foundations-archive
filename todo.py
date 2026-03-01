import json
FILE = "tasks.json"

def load_tasks():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f)

tasks = load_tasks()

while True:
    cmd = input("add/list/quit: ").strip().lower()

    if cmd == "add":
        tasks.append(input("Task: "))
        save_tasks(tasks)

    elif cmd == "list":
        for i, t in enumerate(tasks, 1):
            print(i, t)

    elif cmd == "quit":
        break