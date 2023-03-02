import PySimpleGUI as sg
label_1 = sg.Text("Select files to compress")
input_1 = sg.Input()
button_1 = sg.FilesBrowse("Choose")

label_2 = sg.Text("Select files to compress")
input_2 = sg.Input()
button_2 = sg.FolderBrowse("Choose")

compress = sg.Button("Compress files")

window = sg.Window("File compressor", layout=[[label_1, input_1, button_1],
                                              [label_2, input_2, button_2], [compress]])

window.read()
window.close()
