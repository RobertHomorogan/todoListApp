#from functions import get_todos, write_todos
import functions

while True:
    user_action = input("Type add or show, edit, complete or exit: ")
    user_action = user_action.strip() #removes all spaces

    if user_action.startswith("add"):
        todo = user_action[4:]  #takes the todo from index 4 after the ''add ''

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos): #enumerate function
            item = item.strip("\n")   # remove the spaces in between
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todo = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo '{todo_to_remove}' was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue


    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")

print("Bye")