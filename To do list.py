tasks = []

while True:
    choice = input("p. Add Task\nq. Remove Task\nr. View Tasks\ns. Exit\nEnter your choice: ")
    
    if choice == 'p':
        tasks.append(input("Enter task: "))
    elif choice == 'q':
        task = input("Enter task to remove: ")
        tasks.remove(task) if task in tasks else print("Task not found.")
    elif choice == 'r':
        print("\n".join(tasks) if tasks else "No tasks yet.")
    elif choice == 's':
        break
    else:
        print("Invalid choice.")