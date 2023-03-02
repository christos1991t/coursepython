import PySimpleGUI as sg
import convertfunc as cv

label_1 = sg.Text("Enter Feet")
input_1 = sg.Input(key="feet")
label_2 = sg.Text('Enter Inches')
input_2 = sg.Input(key="inches")
convert_button = sg.Button("Convert")
meters = sg.Text(key="meters")

window = sg.Window("Convertor", layout=[[label_1, input_1],
                                        [label_2, input_2],
                                        [convert_button, meters]])

while True:

    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])
    meters = cv.convert(feet, inches)
    window["meters"].update(value=f"{meters} m")

    match event:
        case sg.WIN_CLOSED:
            break


window.close()
