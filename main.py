while True:
    user_action = input("Type add or show, edit, complete or exit: ")
    user_action = user_action.strip() #removes all spaces

    if "add" in user_action:
        todo = user_action[4:]  #takes the todo from index 4 after the ''add ''

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_action:

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos): #enumerate function
            item = item.strip("\n")   # remove the spaces in between
            row = f"{index + 1}-{item}"
            print(row)

    elif "edit" in user_action:
        number = int(user_action[5:])
        print(number)

        number = number - 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "complete" in user_action:
        number = int(user_action[9:])

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip("\n")
        todos.pop(index)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

        message = f"Todo '{todo_to_remove}' was removed from the list."
        print(message)


    elif "exit" in user_action:
        break

print("Bye")