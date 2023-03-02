import PySimpleGUI as sg
import zip_creator as zcr

sg.theme("Green")

label_1 = sg.Text("Select files to compress")
input_1 = sg.Input()
button_1 = sg.FilesBrowse("Choose Files", key="files")

label_2 = sg.Text("Select destination of files")
input_2 = sg.Input()
button_2 = sg.FolderBrowse("Choose Destination", key="folder")

compress = sg.Button("Compress files")
output_label_1 = sg.Text(key="output", text_color="green")

label_3 = sg.Text("Select archive to extract")
input_3 = sg.Input()
button_3 = sg.FilesBrowse("Choose Archive", key="archive")

extract = sg.Button("Extract files")
output_label_2 = sg.Text(key="output_2", text_color="green")

window = sg.Window("File compressor", layout=[[label_1, input_1, button_1],
                                              [label_3, input_3, button_3],
                                              [label_2, input_2, button_2],
                                              [compress, output_label_1],
                                              [extract, output_label_2]])

while True:
    event, values = window.read()

    filepaths = values["files"].split(';')
    folder = values["folder"]
    archivepath = values["archive"]

    zcr.make_archive(filepaths, folder)
    zcr.extract_archive(archivepath, folder)
    window["output"].update(value="Compression completed")
    window["output_2"].update(value="Extraction completed")


window.close()
