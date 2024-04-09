tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print("Task added to the list.")


def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("\nCurrent Tasks:")
        for i in range(len(tasks)):
            print(f"{i+1} -> {tasks[i]}") 


def deleteTask():
    if len(tasks)==0:
        return
    listTasks() 
    try:
        taskToDelete = int(input("Enter Task No. to delete: "))
        if taskToDelete > 0 and taskToDelete <= len(tasks):
            tasks.pop(taskToDelete-1)
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"Task NO.{taskToDelete} was not found.")
    except:
        print("Invalid input.")



#-------------Main Program -----------
print("Welcome to the to do list app --->")
while True:


    print("\n")
    print("Please select one of the following options")
    print("-----------------------------------------")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List tasks")
    print("4. Quit")

    choice = int(input("Enter your choice: "))

    if (choice == 1):
        addTask()
    elif (choice == 2):
        deleteTask()
    elif (choice == 3):
        listTasks()
    elif (choice == 4):
        print("Application Closed")
        break
    else:
        print("Invalid input. Please try again.")