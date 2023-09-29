List_of_tasks=[]
def tasks_performed():
    print("Tasks performed in the To-do list")
    print("Press 1 for Adding a new Task")
    print("Press 2 for Viewing Tasks")
    print("Press 3 for Marking for showing Task is completed")
    print("Press 4 for Removing a Task")
    print("Press 5 for Exiting")
    print()
    task_selection= input("Select what you want to do: ")
    return task_selection
def adding_new_task():
    print()
    Task=input("Enter the desired Task: ")
    List_of_tasks.append({"Task":Task,"Completed":False})
    print("Task added successfully to the To-do list")
def viewing_tasks():
    print()
    print("Your To-do list")
    for i,Task in enumerate(List_of_tasks, start=1):
        Status_of_Tasks="Completed" if Task["Completed"] else "Not Completed"
        print(f"{i}. {Task['Task']}-{Status_of_Tasks}")
def Tick_marks():
    print()
    viewing_tasks()
    position_of_task=int(input("Enter the Task's position to mark as completed: ")) - 1
    if 0<=position_of_task<len(List_of_tasks):
        List_of_tasks[position_of_task]["Completed"]=True
        print("Task marked as completed!")
    else:
        print("Position entered has no task in it.")
def removal_of_task():
    print()
    viewing_tasks()
    Select_task_number=int(input("Enter the position of the task you want to remove: "))-1
    if 0<=Select_task_number<len(List_of_tasks):
        removing_task=List_of_tasks.pop(Select_task_number)
        print(f"Task '{removing_task['Task']}' removed successfully!")
    else:
        print("Invalid position.")
while True:
    selection_time=tasks_performed()
    if selection_time=='1':
        adding_new_task()
    elif selection_time=='2':
        viewing_tasks()
    elif selection_time=='3':
        Tick_marks()
    elif selection_time=='4':
        removal_of_task()
    elif selection_time=='5':
        print("Khatam, TATA, Bye bye...!")
        break
    else:
        print("Wrong input dio, are you sober rn?")

