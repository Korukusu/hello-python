tasks = []

while True:

    print("\n--- TO DO LIST ---")
    print("1 - Add task")
    print("2 - Show tasks")
    print("3 - Delete task")
    print("4 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(i, "-", task)

    elif choice == "3":
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            tasks.pop(num - 1)
        else:
            print("Invalid task")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option")