from functions import get_todos, write_todos
import PySimpleGUI as sg
from time import strftime
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Reds")

layout = [[sg.Text('', key="clock")],
          [sg.Text("Type in a to-do")],
          [sg.InputText(tooltip="Enter something", key="todo"), sg.Button("Add")],
          [sg.Listbox(values=get_todos(), key="todos",
                      enable_events=True, size=[45, 10]),
           sg.Button("Edit"), sg.Button("Complete")],
          [sg.Button("Exit")]]

window = sg.Window('My To-Do-App',
                   layout,
                   font=("Helvetica", 15))
while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=strftime('%b %d, %Y %H:%M:%S'))
    match event:
        case "Add":
            # Getting value from user
            if values['todo'] != "":
                todos = get_todos()
                new_todo = values['todo']
                todos.append(new_todo + '\n')
                write_todos(todos)

                window['todos'].update(values=todos)
            elif values['todo'] == "":
                sg.popup("Please type something in!", font=("Helvetica", 15))
        case "Edit":
            # skips the first 5 letters in the string to skip edit
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values['todo']
                todos = get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Select an item first!")
                continue
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = get_todos()
                todos.remove((todo_to_complete))
                write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Select an item !", font=("Helvetica", 15))
                continue
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
