import PySimpleGUI as sg
from zip_ceator import make_archive


lable1 = sg.Text('Select File to Compress: ')
input1 = sg.Input()
choose_btn1 = sg.FilesBrowse("Browse", key="files")

lable2 = sg.Text('Select where to create: ')
input2 = sg.Input()
choose_btn2 = sg.FolderBrowse("Select", key="folder")


compress_btn = sg.Button("Compress")
output_lable = sg.Text(key="output", text_color="green")

window = sg.Window("File Ziper by Aryan Kumar Upadhyay", layout=[[lable1,input1,choose_btn1],
                                                                 [lable2,input2,choose_btn2],
                                                                 [compress_btn,output_lable]
                                                                 ])
while True:
    event, values = window.read()
    print(event,values)
    filepaths = values["files"].split(';')
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression Completed!")
    if sg.WIN_CLOSED:
        break
window.close()
