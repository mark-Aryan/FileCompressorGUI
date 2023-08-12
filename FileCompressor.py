import PySimpleGUI as sg

lable1 = sg.Text('Select File to Compress: ')
input1 = sg.Input()
choose_btn1 = sg.FileBrowse("Browse")

lable2 = sg.Text('Select where to create: ')
input2 = sg.Input()
choose_btn2 = sg.FileBrowse("Select")

compress_btn = sg.Button("Compress")

window = sg.Window("File Ziper by Aryan Kumar Upadhyay", layout=[[lable1,input1,choose_btn1],
                                                                 [lable2,input2,choose_btn2],
                                                                 [compress_btn]
                                                                 ])
window.read()
window.close()
