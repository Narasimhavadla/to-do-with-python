# Step 1: Define Functions
def display_list(todo_list):
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")


def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")


def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the list.")
    else:
        print("Invalid task index. Please choose a valid task to remove.")


# Step 2: Implement the Main Function
def main():
    todo_list = []

    while True :
        print("\nTo-Do List Menu:")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            display_list(todo_list)
        elif choice == "2":
            task = input("Enter the task to add: ")
            add_task(todo_list, task)
        elif choice == "3":
            task_index = int(input("Enter the task index to remove: "))
            remove_task(todo_list, task_index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()

# Step 3: Testing (You can test your functions here)
# For example:
# test_list = []
# add_task(test_list, "Task 1")
# display_list(test_list)
# remove_task(test_list, 1)
# display_list(test_list)

# Step 4: Run and Debug
# Run the program and test it with various scenarios as mentioned in Step 3.
# Handle potential errors and edge cases as needed.
