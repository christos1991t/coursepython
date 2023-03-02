import PySimpleGUI as sg
import zip_creator as zcr

label_1 = sg.Text("Select files to compress")
input_1 = sg.Input()
button_1 = sg.FilesBrowse("Choose", key="files")

label_2 = sg.Text("Select files to compress")
input_2 = sg.Input()
button_2 = sg.FolderBrowse("Choose", key="folder")

compress = sg.Button("Compress files")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("File compressor", layout=[[label_1, input_1, button_1],
                                              [label_2, input_2, button_2], [compress, output_label]])

while True:
    event, values = window.read()
    filepaths = values["files"].split(';')
    folder = values["folder"]
    zcr.make_archive(filepaths, folder)
    window["output"].update(value="Compression completed")


window.close()
