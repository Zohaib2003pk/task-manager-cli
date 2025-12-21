tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added:", task)

def show_tasks():
    for i, task in enumerate(tasks, start=1):
        print(i, task)

def delete_task(index):
    tasks.pop(index - 1)

# Testing add-task feature
add_task("Software Construction Assignment")
