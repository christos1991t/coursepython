import PySimpleGUI as sg

label_1 = sg.Text("Enter Feet")
input_1 = sg.Input()
label_2 = sg.Text('Enter Inches')
input_2 = sg.Input()
convert_button = sg.Button("Convert")

window = sg.Window("Convertor", layout=[[label_1, input_1],
                                        [label_2, input_2],
                                        [convert_button]])
window.read()
window.close()
