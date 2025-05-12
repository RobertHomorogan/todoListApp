while True:
    user_action = input("Type add or show, edit, complete or exit: ")
    user_action = user_action.strip() #removes all spaces
    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "show":

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos): #enumerate function
                item = item.strip("\n")   # remove the spaces in between
                row = f"{index + 1}-{item}"
                print(row)

        case "edit":
            print("Edit selected")
            number = int(input("Number of todos to edit: ")) #trabsforming str to int
            number = number - 1

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case"complete":
            number = int(input("Number of todos to complete: "))

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            message = f"Todo '{todo_to_remove}' was removed from the list."
            print(message)


        case "exit":
            break
        case _:
            print("You didn't run any command")
print("Bye")