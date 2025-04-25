

todos = []

while True:
    user_action = input("Type add or show, edit, complete or exit: ")
    user_action = user_action.strip() #removes all speces
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos): #enumerate function
                print(f"{index + 1}-{item}")
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