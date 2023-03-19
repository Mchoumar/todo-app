from functions import get_todos, write_todos
from time import strftime
now_time = strftime("%b %d, %Y %H:%M:%S")
print("It is", now_time)

prompt = "Type add, show, edit, complete, or exit: "
while True:
    user_prompt = input(prompt)
    user_prompt = user_prompt.strip()

    if user_prompt.startswith("add"):
        # Getting value from user
        todo = user_prompt[4:]

        todos = get_todos()
        todos.append(todo + '\n')

        write_todos(todos)

        print(f"{todo} was added to the list!")
    elif user_prompt.startswith("show"):
        # Presenting the values form the file to the user
        todos = get_todos("todos.txt")

        for index, item in enumerate(todos):
            print(f"{index + 1}-{item}", end="")

    elif user_prompt.startswith("edit"):
        # Editing the values inside the file
        try:
            # skips the first 5 letters in the string to skip edit
            number = int(user_prompt[5:]) - 1
            todos = get_todos()
            todos[number] = input("Enter the new todo: ") + '\n'
            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_prompt.startswith("complete"):
        # Removing values from the file
        try:
            # skips the first 9 letters in the string to skip complete
            num = int(user_prompt[9:]) - 1
            todos = get_todos()
            todo_to_remove = todos[num].strip('\n')
            todos.pop(num)
            write_todos(todos)
            print(f"Todo {todo_to_remove} was removed from the list.")
        except ValueError:
            print("Your command is not valid.")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_prompt.startswith("exit"):
        break
    else:
        print("Command is not valid!")
print("Bye!")
