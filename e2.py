# import  webbrowser
#
# user_term = input("Enter the search word: ").replace(" ", "+")
#
# webbrowser.open("https://www.google.com/search?q=" + user_term)
#
import PySimpleGUI as sg

layout = [[sg.Text('Select an image file:'), sg.Input(), sg.FileBrowse()],
          [sg.Image(key='image')]]

window = sg.Window('Image Viewer', layout)

while True:
    event, values = window.Read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Browse':
        filename = values[0]
        window['image'].Update(filename=filename)

window.Close()
