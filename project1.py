'''
# To Do List Application
- use input, variable & stringd
- Lists, sets
- Loops & conditions
- Functions & f-strings
'''

tasks = []
completed_tasks= set()

#add a task
def add_task():
    "Add a new task to the task list"
    task = input("Please enter a new task here -> ")
    tasks.append(task)
    print(f"Task '{task}' added successfully to the task list!.\n")
#view the task
def view_tasks():
    "view all tasks in the task list"
    if not tasks:
        print("No tasks found.\n")
    else:
        print("Here are your tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✅Completed" if task in completed_tasks else "Pending"
            print(f"{i}. {task} - {status}")
#mark task as completed
def mark_task_completed(task_number):
    "Mark a task as completed"
    if 1 <= task_number <= len(tasks):
         task_item = tasks[task_number - 1]
         completed_tasks.add(task_item)
         print(f"Task '{task_item}' marked as completed.\n")
    else:
        print("Invalid task number. Please try again.\n")
#delete a task
def delete_task(task_number):
    "Delete a task from the task list"
    if 1 <= task_number <= len(tasks):
        task_item = tasks.pop(task_number - 1)
        completed_tasks.discard(task_item)
        print(f"Task '{task_item}' deleted successfully from the task list.\n")
    else:
        print("Invalid task number. Please try again.\n")

while True:
        print("""Welcome to the To-Do List Application!
        1. Add a task
        2. View tasks
        3. Mark a task as completed
        4. Delete a task
        5. Exit
        """)
        choice = input("Enter your choice(1-5): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_no = int(input("Enter the task no you to mark it completed ->"))
            mark_task_completed(task_no)
        elif choice == "4":
            task_no = int(input("Enter the task no you to delete the task ->"))
            delete_task(task_no)
        elif choice == "5":
            print("Exiting To-Do app. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")