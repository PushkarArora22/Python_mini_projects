def main():
    tasks=[]
    while True:
            print("=== Personal Task & Productivity Manager ===")
            print("1. Add Task")
            print("2. View All Tasks")
            print("3. Search Tasks")
            print("4. Mark Task as Completed")
            print("5. Remove Task")
            print("6. Filter Tasks")
            print("7. View Productivity Statistics")
            print("8. Exit")
    
            choice=input("\nChoose an option(1-8): ").strip()

            if choice == "1":
                add_task(tasks)
            elif choice == "2":
                view_tasks(tasks)
            elif choice == "3":
                search_task(tasks)
            elif choice == "4":
                mark_completed(tasks)
            elif choice == "5":
                remove_task(tasks)
            elif choice == "6":
                filter_tasks(tasks)
            elif choice == "7":
                show_statistics(tasks)
            elif choice == "8":
                print("\nThanks for using Personal Task & Productivity Manager. Goodbye! 🚀")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 8.\n")


def add_task(tasks):
    task_name=input("Enter the task name: ").strip()

    if not task_name:
        print("Task name cannot be empty.\n")
        return

    for task in tasks:
        if task[0].lower()==task_name.lower():
            print("This task already exists.\n")
            return
    tasks.append([task_name,"Pending"])
    print(f'"{task_name}" added successfully.\n')

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return
    print("Available tasks\n")
   
    for number,task in enumerate(tasks,start=1):
        print(f"{number}. {task[0]} - {task[1]}")




def search_task(tasks):
    search = input("Enter a keyword to search: ").strip().lower()

    found = False

    for task in tasks:
        if search in task[0].lower():
            print(f"{task[0]} - {task[1]}")
            found = True

    if not found:
        print("No match found.")


def filter_tasks(tasks):
    status=input("Filter on the basis of status").strip().lower()
    if status!="pending" and status!="completed":
        print("Enter valid filter")
        return
    for task in tasks:
        if task[1].lower()==status:
            print(f"{task[0]} - {task[1]}")


def mark_completed(tasks):
    if not tasks:
        print("No task available")
        return
    view_tasks(tasks)
    try:
        user=int(input("Enter the task number to mark as completed"))
        if 1<=user<=len(tasks):
            if tasks[user-1][1].lower()=="pending":    
                tasks[user-1][1]="Completed"
                print(f"{tasks[user-1][0]} - {tasks[user-1][1]}")
            else:
                print("Already marked as complete")
        else:
            print("Enter correct task number")
    except ValueError:
        print("Enter valid task number")
            

def remove_task(tasks):
    if not tasks:
        print("No task available")
        return
    view_tasks(tasks)
    try:
        user=int(input("Enter a task number"))
        if 1<=user<=len(tasks):
            tasks.pop(user-1)
            print("Task removed")
        else:
            print("Enter correct task number")
    except ValueError:
        print("Enter a valid task number")


def show_statistics(tasks):
    if not tasks:
        print("No tasks available")
        return
    print(f"Total tasks: {len(tasks)}")
    a=0
    b=0
    for task in tasks:
        if task[1].lower()=="pending":
            a+=1
        else:
            b+=1
    print(f"Completed tasks: {b}")
    print(f"Pending tasks: {a}")
    print(f"Completion rate: {(b/len(tasks))*100} %")


main()

