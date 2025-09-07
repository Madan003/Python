tasks = []

while True:
    print("1. Add task\n2. Remove task\n3. View tasks\n4. Exit ")
    option = int(input("Enter a option: "))

    if option == 1:
        task = input("Enter a task to add: ")
        tasks.append(task)
        print("✅ Task added succesfully.")
    elif option == 2:
        check =input("Are you entering task or index: ")
        if check.lower() == "task":  
            task = input("Enter a task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print("✅ Task removed succesfully.")
            else :
                print("Task not found! ")
        elif check.lower() == "index":
            index = int(input("Enter a task number to remove: "))
            if 1<= index <= len(tasks):
                tasks.pop(index-1)
                print("✅ Task removed succesfully.")
            else:
                print("❌ Invalid task number!")
    elif option == 3:
        if not tasks:
            print("List is empty!.")
        else:
            print("Your tasks: ")
            for i,task in enumerate(tasks,start=1):
                print(f"{i}. {task}")
    elif option == 4:
        if not tasks:
            print("List is empty!.")
        else:
            print("Final To-Do list: ")
            for i,task in enumerate(tasks,start=1):
                print(f"{i}. {task}")
        break
    else :
        print("Error!, Enter a valid option.")