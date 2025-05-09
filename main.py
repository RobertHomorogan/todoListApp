while True:
    user_action = input("Type add or show, edit, complete or exit: ")
    user_action = user_action.strip() #removes all spaces
    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open("todos.txt", "r") #"r" read the file
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("todos.txt", "w")  #"w" writes on the files
            file.writelines(todos)
            file.close()

        case "show":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos): #enumerate function
                item = item.strip("\n")   # remove the spaces in between
                row = f"{index + 1}-{item}"
                print(row)

        case "edit":
            print("Edit selected")
            number = int(input("Number of todos to edit: ")) #trabsforming str to int
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case"complete":
            number = int(input("Number of todos to complete: "))
            todos.pop(number - 1)


        case "exit":
            break
        case _:
            print("You didn't run any command")
print("Bye")