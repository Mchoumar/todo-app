from functions import get_todos, write_todos
import PySimpleGUI as sg
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter something")
add_button = sg.Button("Ok")

window = sg.Window('my To-Do-App', layout=[[label], [input_box, add_button]])
i, v = window.read()
print(v[0])
window.close()
