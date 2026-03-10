tasks = []

while True:

    task = input("Enter a task (or type exit): ")

    if task == "exit":
        break

    tasks.append(task)

print("\nYour tasks:")

for i, task in enumerate(tasks, 1):
    print(i, "-", task)