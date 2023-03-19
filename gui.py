from functions import get_todos, write_todos
import PySimpleGUI as sg
layout = [[sg.Text("Type in a to-do")],
          [sg.InputText(tooltip="Enter something", key="todo"), sg.Button("Add")],
          [sg.Button("Close")]]

window = sg.Window('My To-Do-App',
                   layout,
                   font=("Helvetica", 15))
while True:
    event, value = window.read()
    match event:
        case "Add":
            # Getting value from user

            todos = get_todos()
            new_todo = value['todo']
            todos.append(new_todo + '\n')
            write_todos(todos)

            print(f"{new_todo} was added to the list!")
        case "Close":
            break

window.close()
