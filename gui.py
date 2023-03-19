from functions import get_todos, write_todos
import PySimpleGUI as sg
layout = [[sg.Text("Type in a to-do")],
          [sg.InputText(tooltip="Enter something", key="todo"), sg.Button("Add")],
          [sg.Listbox(values=get_todos(), key="todos",
                      enable_events=True, size=[45, 10]), sg.Button("Edit")]]

window = sg.Window('My To-Do-App',
                   layout,
                   font=("Helvetica", 15))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            # Getting value from user

            todos = get_todos()
            new_todo = values['todo']
            todos.append(new_todo + '\n')
            write_todos(todos)

            window['todos'].update(values=todos)
        case "Edit":
            # skips the first 5 letters in the string to skip edit
            todo_to_edit = values["todos"][0]
            new_todo = values['todo']
            todos = get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
