filename = "tasks.txt"

try:
    with open(filename, "r") as f:
        tasks = [line.strip() for line in f]
except FileNotFoundError:
    tasks = []

while True:
    print("\nTo-Do List")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if not tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        with open(filename, "a") as f:
            f.write(new_task + "\n")
        print("Task added.")

    elif choice == "3":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        try:
            num = int(input("Enter task number to remove: ")) - 1
            if 0 <= num < len(tasks):
                removed = tasks.pop(num)
                with open(filename, "w") as f:
                    for task in tasks:
                        f.write(task + "\n")
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        print("BYE!")
        break

    else:
        print("Invalid option. Try again.")
