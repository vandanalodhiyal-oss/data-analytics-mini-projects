# To-Do List App----

tasks = []   # All tasks store 

while True:                    # Infinite loop----
    print("\n1. Add Task")     # Menu show-----
    print("2. View Tasks")
    print("3. Exit")
    
    choice = input("Enter your choice: ")  

    # Add Task------
    if choice == "1":
        task = input("Enter your task: ")  
        tasks.append(task)                  # Task list me add karna
        print("Task added successfully!")

    # View Tasks------
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available")   # Agar list empty hai
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i+1, ".", tasks[i])   # Task number ke saath print

     #  Exit
    elif choice == "3":
        print("Thank you!")
        break   # Loop stop

    