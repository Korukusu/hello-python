tasks = []

task1 = input("Enter task: ")
tasks.append(task1)

task2 = input("Enter another task: ")
tasks.append(task2)

print("Your tasks:")

for task in tasks:
    print("-", task)